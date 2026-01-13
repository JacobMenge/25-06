const products = [
  { name: 'Laptop', price: 999 },
  { name: 'Mouse', price: 29 },
  { name: 'Monitor', price: 299 }
];

const expensive = products.filter(p => p.price > 400);


console.table(expensive);