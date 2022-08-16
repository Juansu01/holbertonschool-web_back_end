function calculateNumber(type, a, b) {

  if (type === 'DIVIDE') {
      if (a === 0 || b === 0) {
        return 'Error';
      }
    return Math.round(a) / Math.round(b);
  }

  if (type === 'SUM') {
    return Math.round(a) + Math.round(b);
  }

  return Math.round(a) - Math.round(b);

}

module.exports = calculateNumber;
