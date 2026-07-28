const express = require("express");
const bodyParser = require("body-parser");
const axios = require("axios");

const app = express();

app.use(bodyParser.urlencoded({ extended: true }));

app.get("/", (req, res) => {
  res.send(`
    <h2>Flask Todo Frontend</h2>
    <form action="/submit" method="POST">
      <input type="text" name="task" placeholder="Enter Task" required>
      <button type="submit">Submit</button>
    </form>
  `);
});

app.post("/submit", async (req, res) => {
  try {
    const response = await axios.post(
      "http://backend:5000/submittodoitem",
      {
        task: req.body.task
      }
    );

    res.send(response.data);
  } catch (error) {
    res.send("Backend connection failed.");
  }
});app.listen(3000, "0.0.0.0", () => {
  console.log("Frontend running on port 3000");
});