// In Stock
import express from 'express';
import redis from 'redis';
import { promisify } from 'util';

const listProducts = [
  {
    id: 1,
    name: 'Suitcase 250',
    price: 50,
    stock: 4,
  },
  {
    id: 2,
    name: 'Suitcase 450',
    price: 100,
    stock: 10,
  },
  {
    id: 3,
    name: 'Suitcase 650',
    price: 350,
    stock: 2,
  },
  {
    id: 4,
    name: 'Suitcase 1050',
    price: 550,
    stock: 5,
  },
];
// export default listProducts;

// Data access
export default function getItemById(id) {
  return listProducts[id - 1];
}

// Server
const app = express();
const hostname = '127.0.0.1';
const port = 1245;

// Products
app.get('/list_products', (req, res) => {
  const newListProducts = [];
  listProducts.forEach((product) => {
    const {
      id: itemId, name: itemName, price, stock: initialAvailableQuantity,
    } = product;
    const newProduct = {
      itemId, itemName, price, initialAvailableQuantity,
    };
    newListProducts.push(newProduct);
  });
  res.status(200).send(newListProducts);
});

app.listen(port, hostname);

// In stock in redis
const client = redis.createClient();
client.on('error', (err) => console.log('Redis client not connected to the server:', err.message));
client.on('ready', () => console.log('Redis client connected to the server'));

function reserveStockById(itemId, stock) {
  // set redis stock level for a given item id
  client.set(`item.${itemId}`, stock, redis.print);
}

async function getCurrentReservedStockById(itemId) {
  // return the reserved stock for a given item based on the itemId
  const asyncGet = promisify(client.get).bind(client);
  const result = await asyncGet(`item.${itemId}`);
  // console.log(result);
  return result;
}

reserveStockById(3, 1);
app.get('/list_products/:itemId', async (req, res) => {
  // get a route for list of products based on an item id
  const id = parseInt(req.params.itemId, 10);
  if (Number.isNaN(id)) {
    res.status(400).send({ status: 'Product not found' });
    return;
  }
  try {
    const reservedQuantity = await getCurrentReservedStockById(id);
    const product = listProducts[id - 1];
    const {
      id: itemId, name: itemName, price, stock: initialAvailableQuantity,
    } = product;
    const newProduct = {
      itemId, itemName, price, initialAvailableQuantity,
    };
    // newProduct['currentQuantity'] = currentQuantity;
    const currentQuantity = reservedQuantity
      ? newProduct.initialAvailableQuantity - reservedQuantity
      : newProduct.initialAvailableQuantity;
    newProduct.currentQuantity = currentQuantity;
    res.status(200).send(newProduct);
  } catch (err) {
    res.status(400).send({
      status: 'Product not found',
    });
  }
});

app.get('/reserve_product/:itemId', async (req, res) => {
  // route for reserving a product
  const id = parseInt(req.params.itemId, 10);
  if (Number.isNaN(id)) {
    res.status(400).send({
      status: 'Product not found',
    });
    return;
  }
  try {
    const reservedQuantity = await getCurrentReservedStockById(id);
    const product = listProducts[id - 1];
    const {
      id: itemId, name: itemName, price, stock: initialAvailableQuantity,
    } = product;
    const newProduct = {
      itemId, itemName, price, initialAvailableQuantity,
    };
    // newProduct['currentQuantity'] = currentQuantity;
    const currentQuantity = reservedQuantity
      ? newProduct.initialAvailableQuantity - reservedQuantity
      : newProduct.initialAvailableQuantity;
    newProduct.currentQuantity = currentQuantity;
    if (currentQuantity <= 0) {
      // rserve 1
      res.status(400).send({
        status: 'Not enough stock available', itemId: id,
      });
      return;
    }
    reserveStockById(id, 1);
    res.status(200).send({
      status: 'Reservation confirmed', itemId: id,
    });
    return;
  } catch (err) {
    // console.log('Error:', err);
    res.status(400).send({ status: 'Product not found' });
  }
});
