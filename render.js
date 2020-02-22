const mp3Duration = require('mp3-duration')
const {render} = require('@nexrender/core')

const FPS = 23.976;

const job = {
    template: {
		src:'file:///AutomationRender/Video.aep',
		composition:'Main',
		frameStart:0,
		frameEnd: 1000
    },
    assets: [
        {
            src: 'file:///AutomationRender/image.jpg',
            type: 'image',
			layerName:'image.jpg'
        },
        {
			src:'file:///AutomationRender/audio.mp3',
			type:'audio',
			layerName:'audio.mp3'
        },
		{
			type:'data',
			layerName:'ProgressLine',
			property:'Scale',
			expression:'audioLayer = thisComp.layer(\'audio.mp3\');beginTime = audioLayer.startTime;endTime = audioLayer.source.duration;startScale = [0,391];endScale = [45,391];linear(time,beginTime,endTime,startScale,endScale);'
        },
		{
			type:'data',
			layerName:'image.jpg',
			property:'Position',
			expression:'var w=thisComp.width;var h=thisComp.height;var w2=w/2;var h2=h/2;[w2,h2]'
		},
		{
			type:'data',
			layerName:'image.jpg',
			property:'Scale',
			expression:'sizeX = 100*thisComp.width/thisLayer.width;[sizeX+2, sizeX+2]'
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
				output:'C:/AutomationRender/output.mp4'
			}
		]
	},

    onRenderProgress: (job, value) => console.log('onRenderProgress:', value)
}

mp3Duration('C:/AutomationRender/audio.mp3', async function (err, duration) {
    job.template.frameEnd = Math.ceil(FPS * duration);
    const result = await render(job)
    console.log(result)
});
