function hasValuesFromArray(set, array) {
  const isTrue = array.every((item) => set.has(item));
  return isTrue;
}

export default hasValuesFromArray;
