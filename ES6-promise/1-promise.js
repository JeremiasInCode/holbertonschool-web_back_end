export default function getResponseFromAPI(success) {
  return new Promise((resolve, reject) => {
    if (success) {
      return resolve({
        status: 200,
        body: ''
      })
    }
    return reject (
      new Error('The fake API is not working currently')
    )
  });
}
