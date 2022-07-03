const { PythonShell } = require("python-shell");
exports.getLastMessages = async (guildId, channelsId, numberOfLastMessages) => {
  // channelsId -> separated with , like example "420147899096104961,682659012902518805" or "420147899096104961"
  let ret = [];
  const res = await pythonrun([
    "--guildId",
    guildId,
    "--channelsId",
    channelsId,
    "--justLastMessages",
    numberOfLastMessages,
  ]);
  if (!res.success) {
    console.log(res.err);
    return false;
  }
  const list = res.results;

  for (var xc = 0; xc < list.length; xc++) {
    if (list[xc] == "lastmessage") {
      const json = list[xc + 1].substring(2, list[xc + 1].length - 1);
      const jsonparse = JSON.parse(json);
      ret.push(...jsonparse);
    }
  }

  return ret;
};

pythonrun = async (argsx) => {
  let args = [
    "--fromD",
    "2022-05-25",
    "--configFile",
    "../../config.json",
    "--tokenFile",
    "../../token.token",
    "--mongoFile",
    "../../mongodb.con",
  ];
  args.push(...argsx);

  const options = {
    args,
  };

  const {
    success,
    err = "",
    results,
  } = await new Promise((resolve, reject) => {
    PythonShell.run("../../discord.py", options, function (err, results) {
      if (err) {
        reject({ success: false, err });
      }
      resolve({ success: true, results });
    });
  });

  return {
    success,
    err,
    results,
  };
};
