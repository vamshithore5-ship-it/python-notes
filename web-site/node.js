app.post("/appointments", (req, res) => {
  const { patientName, email, doctor, date } = req.body;
  console.log("Appointment booked:", patientName, doctor, date);
  res.send({ message: "Appointment successfully booked!" });
});
