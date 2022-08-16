function calculateNumber(type, a, b) {

  if (type === 'DIVIDE') {
    return Math.round(a) / Math.round(b);
  }

  if (type === 'SUM') {
    return Math.round(a) + Math.round(b);
  }

  return Math.round(a) - Math.round(b);

}

module.exports = calculateNumber;
