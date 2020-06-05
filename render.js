const mp3Duration = require('mp3-duration')
const {render} = require('@nexrender/core')

const FPS = 23.976;

const job = {
    template: {
		src:'file:///Video.aep',
		composition:'Main',
		frameStart:0,
		frameEnd: 2
    },
    assets: [
        {
            src: 'file:///image.jpg',
            type: 'image',
			layerName:'image.jpg'
        },
    ],
	actions:{
		postrender:[
			{
				module:'@nexrender/action-encode',
				preset:'mp4',
				output:'encoded.mp4'
			},
			{
				module:'@nexrender/action-copy',
				input:'encoded.mp4',
				output:'output.mp4'
			}
		]
	},

    onRenderProgress: (job, value) => console.log('onRenderProgress:', value)
}

mp3Duration('audio.mp3', async function (err, duration) {
    job.template.frameEnd = Math.ceil(FPS * duration);
    const result = await render(job)
    console.log(result)
});
