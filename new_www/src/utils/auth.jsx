const getAuthDetails = function() {
  const authToken = localStorage.getItem("authToken")
  const authUserId = localStorage.getItem("authUserId")
  if (authToken) {
    return {
      token: authToken,
      userId: authUserId
    }
  }
  return null
}


module.exports = getAuthDetails
