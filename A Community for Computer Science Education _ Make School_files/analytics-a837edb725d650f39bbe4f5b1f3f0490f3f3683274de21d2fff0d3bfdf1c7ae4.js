!function(){var t=window.analytics=window.analytics||[];if(!t.initialize){if(t.invoked)return void(window.console&&console.error&&console.error("Segment snippet included twice."));t.invoked=!0,t.methods=["trackSubmit","trackClick","trackLink","trackForm","pageview","identify","reset","group","track","ready","alias","debug","page","once","off","on"],t.factory=function(e){return function(){var n=Array.prototype.slice.call(arguments);return n.unshift(e),t.push(n),t}};for(var e=0;e<t.methods.length;e++){var n=t.methods[e];t[n]=t.factory(n)}t.load=function(t){var e=document.createElement("script");e.type="text/javascript",e.async=!0,e.src=("https:"===document.location.protocol?"https://":"http://")+"cdn.segment.com/analytics.js/v1/"+t+"/analytics.min.js";var n=document.getElementsByTagName("script")[0];n.parentNode.insertBefore(e,n)},t.SNIPPET_VERSION="4.0.0",gon.impersonating||t.load(gon.ENV.SEGMENT_ANALYTICS_ID),t.page()}}();