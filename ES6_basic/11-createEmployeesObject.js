export default function createEmployeesObject(departmentName, employees) {
  const employeesObj = {
    [`${departmentName}:`]: [...employees]
  }
}
