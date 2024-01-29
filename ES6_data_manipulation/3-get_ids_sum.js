export default function getStudentIdsSum(getListStudents) {
  const idsStudents = getListStudents.map((idFinder) => idFinder.id);
  const idsSummed = idsStudents.reduce((acum, actualNumber) => acum + actualNumber, 0);
  return idsSummed
}
