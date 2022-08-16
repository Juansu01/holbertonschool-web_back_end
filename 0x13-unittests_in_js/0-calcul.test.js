const assert = require('assert');
const calculateNumber = require('./0-calcul');

describe('calculateNumber', function () {
  describe('Two Integers', function () {
    it('should return 5', function () {
      assert.strictEqual(calculateNumber(2, 3), 5);
    });
  });

  describe('Integer and float', function () {
    it('should return 7', function () {
      assert.strictEqual(calculateNumber(2, 4.7), 7);
    });
  });

  describe('Two floats', function () {
    it('should return 4', function () {
      assert.strictEqual(calculateNumber(2.2, 2.1), 4);
    });
  });

  describe('Two floats 2', function () {
    it('should return 9', function () {
      assert.strictEqual(calculateNumber(3.8, 4.9), 9);
    });
  });

});
