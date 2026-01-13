const products = [
  { name: 'Laptop', price: 999, inStock: true },
  { name: 'Mouse', price: 29, inStock: true },
  { name: 'Keyboard', price: 79, inStock: false },
  { name: 'Monitor', price: 299, inStock: true }
];

const available = products
  .filter(p => p.inStock)
  .filter(p => p.price < 500)
  .map(p => p.name)
  .sort();


// ['Monitor', 'Mouse' ]

console.log(available);