document.getElementById("contactForm").addEventListener("submit", function(e) {
  e.preventDefault();
  alert("Thank you for contacting us!");
});
app.post("/admin/login", (req, res) => {
  const { username, password } = req.body;
  if (username === "admin" && password === "secure123") {
    res.send({ status: "success", message: "Welcome Admin!" });
  } else {
    res.status(401).send({ status: "fail", message: "Invalid credentials" });
  }
});
