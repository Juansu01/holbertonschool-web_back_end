const weakMap = new WeakMap();
let called = 1;

function queryAPI(endpoint) {

  weakMap.set(endpoint, called);
  called += 1;
  const query = weakMap.get(endpoint);
  if (query >= 5) {
    throw new Error('Endpoint load is high');
  }
}

export { queryAPI, weakMap };
