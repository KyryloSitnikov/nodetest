const { Telegraf } = require('telegraf');
const bot = new Telegraf('6130614504:AAHYFuTbmbNtflJFiUqwsra_vipxSNjRyLA');

const responses = {
    '1': 'My name is Bot',
    '2': new Date().toLocaleTimeString(),
    '3': 'I am doing well, thanks for asking!'
  };

  bot.on('text', (ctx) => {
    const question = ctx.message.text;
    
    if (responses[question]) {
      ctx.reply(responses[question]);
    }
  });