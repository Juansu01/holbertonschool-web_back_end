export default function iterateThroughObject(reportWithIterator) {
  const employees = [];
  for (const report of reportWithIterator) {
    employees.push(report);
  }

  return employees.join(' | ');
}
