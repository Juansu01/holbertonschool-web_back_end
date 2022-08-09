function getListStudentIds(students) {
  if (Array.isArray(students)) {
    const ids = students.map((e) => e.id);
    return ids;
  }

  return [];

}

export default getListStudentIds;
