module.exports = {
    name: 'ping',
    description: 'ping Command',
    execute(message, args) {
        message.channel.send('Pong!');
    },
};