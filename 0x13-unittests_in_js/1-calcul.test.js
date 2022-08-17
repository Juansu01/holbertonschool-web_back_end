const assert = require('assert').strict;
const calculateNumber = require('./1-calcul');

describe('calculateNumber', function () {
  describe('No rounding sum', function () {
    it('should return 6', function () {
      assert.equal(calculateNumber('SUM', 3, 3), 6);
    });
  });

  describe('No rounding sub', function () {
    it('should return 6', function () {
      assert.equal(calculateNumber('SUBTRACT', 5, 2), 3);
    });
  });

  describe('No rounding divide', function () {
    it('should return 1', function () {
      assert.equal(calculateNumber('SUBTRACT', 3, 3), 1);
    });
  });

  describe('Rounding sum', function () {
    it('should return 8', function () {
      assert.equal(calculateNumber('SUM', 3.8, 3.9), 8);
    });
  });

  describe('Division by 0', function () {
    it('should return error', function () {
      assert.equal(calculateNumber('DIVIDE', 2, 0), 'Error');
    });
  });

});
