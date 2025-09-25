const express = require("express");
const path = require("path");
const app = express();

app.use(express.static(path.join(__dirname, "public")));
app.use(express.json());

app.post("/contact", (req, res) => {
  const { name, email, message } = req.body;
  console.log("Contact form submitted:", name, email, message);
  res.send({ status: "success" });
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});
