function updateUniqueItems(map) {
  if ((map instanceof Map)) {
    for (const [key] of map) {
      if (map.get(key) === 1) map.set(key, 100);
    }

  return map;
  }

  throw Error('Cannot process');
}

export default updateUniqueItems;
