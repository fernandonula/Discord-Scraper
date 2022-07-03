const express = require("express");
const cors = require("cors");
const bodyParser = require("body-parser");
const dotenv = require("dotenv-flow");
const env =
  process.env.APPLICATION_ENV || process.env.NODE_ENV || "development";
dotenv.config({
  node_env: env,
});
const routes = require("./routes");

const app = express();
const port = process.env.PORT;

app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());
app.use(bodyParser.text());

app.use(cors({ origin: "*" }));

app.get("/", async (req, res) => {
  res.send("discord scraper api");
});
routes(app);

app.listen(port, () => {
  console.log(`⚡️[server]: Server is running at https://localhost:${port}`);
});
