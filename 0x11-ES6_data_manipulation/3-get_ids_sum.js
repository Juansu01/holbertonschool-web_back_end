function getStudentIdsSum(students) {
  if (Array.isArray(students)) {
    const reducer = (acc, item) => acc + item.id;
    const sum = students.reduce(reducer, 0);

    return sum;
  }
  return [];
}

export default getStudentIdsSum;
