export const weakMap = new WeakMap();

function queryAPI(endpoint) {
  if (weakMap.has(endpoint)) {
    const query = weakMap.get(endpoint);

    if (query >= 4) throw new Error('Endpoint load is high');
    weakMap.set(endpoint, weakMap.get(endpoint) + 1);
  } else {
    weakMap.set(endpoint, 1);
  }
}

export { queryAPI, weakMap };
