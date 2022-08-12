function getStudentsByLocation(students, city) {
  if (Array.isArray(students)) {
    const res = students.filter((e) => e.location === city);

    return res;
  }
  return [];
}

export default getStudentsByLocation;
