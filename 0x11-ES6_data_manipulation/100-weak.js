export const weakMap = new WeakMap();

function queryAPI(endpoint) {
  let timesCalled = weakMap.get(endpoint) || 0;

  timesCalled += 1;

  weakMap.set(endpoint, timesCalled);

  if (timesCalled >= 5) {
    throw Error('Endpoint load is high');
  }

  return timesCalled;
}

export default queryAPI;
