const Service = require("./service");
const service = new Service();

const routes = (app) => {
  app.get("/lastMessages/:guildId/:channelId", async (req, res) => {
    lastMessages(req, res);
  });
};

async function lastMessages(req, res) {
  try {
    let { guildId, channelId } = req.params;
    if (!guildId || !channelId)
      throw Error("You need to send a guildId and channelId.");

    const ret = await service.lastMessages(guildId, channelId);
    res.send(ret);
  } catch (e) {
    console.log(e);
    res.send(e);
  }
}

module.exports = routes;
