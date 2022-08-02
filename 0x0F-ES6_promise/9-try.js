function guardrail(mathFunction) {
  let res;
  const queue = [];

  try {
    res = mathFunction();
  } catch (err) {
    res = err.toString();
  }

  queue.push(res);
  queue.push('Guardrail was processed');
  return queue;
}

export default guardrail;