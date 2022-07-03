const discordScraperModule = require("discordScraperModule");

class Service {
  constructor() {}

  async lastMessages(guildId, channelId) {
    return await discordScraperModule.getLastMessages(guildId, channelId, 3);
  }
}

module.exports = Service;
