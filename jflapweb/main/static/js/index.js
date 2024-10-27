// // Init the cheerpj system.
;(async function () {
  await cheerpjInit()

  var surface = document.getElementById('surface')
  cheerpjCreateDisplay(-1, -1, surface)

  await cheerpjRunJar('/app/resources/jflap-7.0.jar')
})()

// Removing the javascript-disabled alert.

alert = document.getElementById('javascript-disabled')
alert.parentNode.removeChild(alert)
