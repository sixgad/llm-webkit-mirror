html = """
<!DOCTYPE html>


    <html itemscope itemtype="https://schema.org/QAPage" class="html__responsive " lang="en">

    <head>

        <title>How to get current value of Android&#39;s proximity sensor? - Stack Overflow</title>
        <link rel="shortcut icon" href="https://cdn.sstatic.net/Sites/stackoverflow/Img/favicon.ico?v=ec617d715196">
        <link rel="apple-touch-icon" href="https://cdn.sstatic.net/Sites/stackoverflow/Img/apple-touch-icon.png?v=c78bd457575a">
        <link rel="image_src" href="https://cdn.sstatic.net/Sites/stackoverflow/Img/apple-touch-icon.png?v=c78bd457575a"> 
        <link rel="search" type="application/opensearchdescription+xml" title="Stack Overflow" href="/opensearch.xml">
        <link rel="canonical" href="https://stackoverflow.com/questions/35302978/how-to-get-current-value-of-androids-proximity-sensor" />
    <meta name="viewport" content="width=device-width, height=device-height, initial-scale=1.0, minimum-scale=1.0">
        <meta name="bingbot" content="noarchive">         
        <meta property="og:type" content= "website" />
        <meta property="og:url" content="https://stackoverflow.com/questions/35302978/how-to-get-current-value-of-androids-proximity-sensor"/>
        <meta property="og:site_name" content="Stack Overflow" />
        <meta property="og:image" itemprop="image primaryImageOfPage" content="https://cdn.sstatic.net/Sites/stackoverflow/Img/apple-touch-icon@2.png?v=73d79a89bded" />
        <meta name="twitter:card" content="summary"/>
        <meta name="twitter:domain" content="stackoverflow.com"/>
        <meta name="twitter:title" property="og:title" itemprop="name" content="How to get current value of Android&#x27;s proximity sensor?" />
        <meta name="twitter:description" property="og:description" itemprop="description" content="Is it possible to get the current value of the Proximity Sensor in Android?  &#xA;&#xA;I know that I can use SensorManager and Sensor and register a state changed listener, but I have no need to be notifie..." />
    <script id="webpack-public-path" type="text/uri-list">https://cdn.sstatic.net/</script>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.7.1/jquery.min.js"></script>
    <script defer src="https://cdn.sstatic.net/Js/third-party/npm/@stackoverflow/stacks/dist/js/stacks.min.js?v=fe3ef2b1305f"></script>
    <script src="https://cdn.sstatic.net/Js/stub.en.js?v=44cbb4d4d062"></script>

    <link rel="stylesheet" type="text/css" href="https://cdn.sstatic.net/Shared/stacks.css?v=1e9dfb1f6199">
    <link rel="stylesheet" type="text/css" href="https://cdn.sstatic.net/Sites/stackoverflow/primary.css?v=90f1fc95eb69">


    
            <link rel="alternate" type="application/atom+xml" title="Feed for question &#x27;How to get current value of Android&#x27;s proximity sensor?&#x27;" href="/feeds/question/35302978">
        <script>
            StackExchange.ready(function () {

                    StackExchange.using("snippets", function () {
                        StackExchange.snippets.initSnippetRenderer();
                    });
                    
                StackExchange.using("postValidation", function () {
                    StackExchange.postValidation.initOnBlurAndSubmit($('#post-form'), 2, 'answer');
                });


                StackExchange.question.init({showAnswerHelp:true,showTrendingSortLaunchPopover:false,showTrendingSortPostLaunchPopover:false,totalCommentCount:0,shownCommentCount:0,enableTables:true,questionId:35302978});

                styleCode();

                    StackExchange.realtime.subscribeToQuestion('1', '35302978');
                    StackExchange.using("gps", function () { StackExchange.gps.trackOutboundClicks('#content', '.js-post-body'); });


            });
        </script>

        
        
        
        <link rel="stylesheet" type="text/css" href="https://cdn.sstatic.net/Shared/Channels/channels.css?v=5981bb1a5bd7">

        
        

    


    <script type="application/json" data-role="module-args" data-module-name="Shared/options.mod">{"options":{"locale":"en","serverTime":1734583726,"routeName":"Questions/Show","stackAuthUrl":"https://stackauth.com","networkMetaHostname":"meta.stackexchange.com","site":{"name":"Stack Overflow","description":"Q\u0026A for professional and enthusiast programmers","isNoticesTabEnabled":true,"enableNewTagCreationWarning":true,"insertSpaceAfterNameTabCompletion":false,"id":1,"cookieDomain":".stackoverflow.com","childUrl":"https://meta.stackoverflow.com","negativeVoteScoreFloor":null,"enableSocialMediaInSharePopup":true,"protocol":"https"},"user":{"fkey":"3263e220c9fc053cefe5230c13d734e7914d13795116a71a9d8e74c9e9fe345a","tid":"a8aaef07-713b-55ec-e55b-b6b0f1bb9d33","rep":0,"isAnonymous":true,"isAnonymousNetworkWide":true,"ab":{"mobile_signup_link":{"v":"question_assistant","g":2}}},"events":{"postType":{"question":1},"postEditionSection":{"title":1,"body":2,"tags":3}}}}</script>
<script type="application/json" data-role="module-args" data-module-name="Shared/settings.mod">{"settings":{"flags":{"allowRetractingCommentFlags":true,"allowRetractingFlags":true},"questionLinkTitleReplacement":{"maxNumberOfSitesProcessed":10,"maxReplacementsPerSite":20},"search":{},"tags":{},"comments":{},"site":{"allowImageUploads":true,"enableUserHovercards":true,"forceHttpsImages":true,"enableImageHttps":true,"styleCode":true,"stacksEditorPreviewEnabled":true},"subscriptions":{"defaultFreemiumMaxTrueUpSeats":50,"defaultMaxTrueUpSeats":1000,"defaultBasicMaxTrueUpSeats":250},"paths":{"jQueryUICSSPath":"https://ajax.googleapis.com/ajax/libs/jqueryui/1.12.0/themes/smoothness/jquery-ui.css","jQueryUIJSPath":"https://ajax.googleapis.com/ajax/libs/jqueryui/1.12.0/jquery-ui.min.js"},"image":{"maxImageUploadSizeInBytesAnimatedGif":2097152,"maxImageUploadSizeInBytes":10485760},"legal":{"useCustomConsent":false,"oneTrustTCFConfigId":"c3d9f1e3-55f3-4eba-b268-46cee4c6789c"},"userMessaging":{"showNewFeatureNotice":true},"mentions":{"maxNumUsersInDropdown":50},"intercom":{"appId":"inf0secd"},"markdown":{"enableTables":true},"elections":{"opaVoteResultsBaseUrl":"https://www.opavote.com/results/"},"auth":{"oauthInPopup":true},"accounts":{"currentPasswordRequiredForChangingStackIdPassword":true},"questions":{"enableSavesFeature":true,"questionTitleLengthStartLiveWarningChars":50,"maxTitleSize":150,"enableQuestionTitleLengthLiveWarning":true},"snippets":{"snippetsEnabled":true,"renderDomain":"stacksnippets.net"}}}</script>
<script>StackExchange.init();</script>

    <script>
        StackExchange.using.setCacheBreakers({"Js/adops.en.js":"6da43f5e0a84","Js/ask.en.js":"","Js/begin-edit-event.en.js":"20edbaccceae","Js/copy-transpiled.en.js":"7959520085c5","Js/events.en.js":"","Js/explore-qlist.en.js":"ee2a4f8c3992","Js/full-anon.en.js":"756e9cf92803","Js/full.en.js":"33fc8c618f7b","Js/highlightjs-loader.en.js":"dec53251ce5d","Js/inline-tag-editing.en.js":"8517756a2cb6","Js/keyboard-shortcuts.en.js":"c255a5a5979b","Js/markdown-it-loader.en.js":"5818ef89ff9d","Js/mentions-transpiled.en.js":"54b80f913964","Js/moderator.en.js":"562010d1ea7c","Js/postCollections-transpiled.en.js":"fd1c4a681d04","Js/post-validation.en.js":"6c596a8d33b1","Js/question-editor.en.js":"","Js/review-v2-transpiled.en.js":"b80294337dec","Js/revisions.en.js":"9dd135bb585f","Js/stacks-editor.en.js":"8de4a63a68e8","Js/tageditor.en.js":"4d22c6090e5a","Js/tageditornew.en.js":"4554c63a5fa6","Js/tagsuggestions.en.js":"d9e40cbceb75","Js/unlimited-transpiled.en.js":"8713a979101d","Js/wmd.en.js":"8e5e21c8ea03","Js/snippet-javascript-codemirror.en.js":"8aaa42d59dbc"});
        StackExchange.using("gps", function() {
             StackExchange.gps.init(true);
        });
    </script>
    <noscript id="noscript-css"><style>body,.s-topbar{margin-top:1.9em}</style></noscript>
    </head>
    <body class="question-page unified-theme">

        
<div id="signup-modal-container"></div>
<script type="application/json" data-role="module-args" data-module-name="islands/signup-modal/index.mod">{"ContainerElementId":"signup-modal-container","FKey":"3263e220c9fc053cefe5230c13d734e7914d13795116a71a9d8e74c9e9fe345a","TriggerEvent":"signupModalShow","OauthInPopup":true,"ReturnUrl":"https://stackoverflow.com/questions/35302978/how-to-get-current-value-of-androids-proximity-sensor","ReturnUrlForPopup":"https://stackoverflow.com/users/after-signup/oauth-only","SiteName":"Stack Overflow","SiteLogoPath":"https://cdn.sstatic.net/Sites/stackoverflow/Img/icon-48.png?v=b7e36f88ff92","AuthProviders":["Google","GitHub"],"ParentSiteUrl":"","IsInitiallyVisible":false}</script>
<script defer src="https://cdn.sstatic.net/Js/webpack-chunks/svelte.en.js?v=150134e89426"></script><script defer src="https://cdn.sstatic.net/Js/webpack-chunks/stacks-svelte.en.js?v=72feec5d5528"></script><script defer src="https://cdn.sstatic.net/Js/webpack-chunks/1315.en.js?v=d971ebf7a8e2"></script><script defer src="https://cdn.sstatic.net/Js/webpack-chunks/4537.en.js?v=e6769247457b"></script><script defer src="https://cdn.sstatic.net/Js/islands/signup-modal.en.js?v=70d42243ade4"></script>

<script defer>
    dispatchEvent(new CustomEvent("openSignupModal"));
</script>
    
        <div id="one-tap-container"></div>
<script type="application/json" data-role="module-args" data-module-name="islands/one-tap/index.mod">{"ContainerElementId":"one-tap-container","FKey":"3263e220c9fc053cefe5230c13d734e7914d13795116a71a9d8e74c9e9fe345a","GoogleClientId":"717762328687-iludtf96g1hinl76e4lc1b9a82g457nn.apps.googleusercontent.com","Autoselect":false,"ReturnUrl":"https%3a%2f%2fstackoverflow.com%2fquestions%2f35302978%2fhow-to-get-current-value-of-androids-proximity-sensor"}</script><script defer src="https://cdn.sstatic.net/Js/webpack-chunks/svelte.en.js?v=150134e89426"></script><script defer src="https://cdn.sstatic.net/Js/islands/one-tap.en.js?v=661858832214"></script>    <div id="notify-container"></div>
    <div id="custom-header"></div>
        

<header class="s-topbar ps-fixed t0 l0 js-top-bar">
    <a href="#content" class="s-topbar--skip-link">Skip to main content</a>
	<div class="s-topbar--container">
			<a href="#" class="s-topbar--menu-btn js-left-sidebar-toggle" role="menuitem" aria-haspopup="true" aria-controls="left-sidebar" aria-expanded="false"><span></span></a>
			<div class="topbar-dialog leftnav-dialog js-leftnav-dialog dno">
				<div class="left-sidebar js-unpinned-left-sidebar" data-can-be="left-sidebar" data-is-here-when="sm"></div>
			</div>
				<a href="https://stackoverflow.com" class="s-topbar--logo js-gps-track"
		   data-gps-track="top_nav.click({is_current:false, location:2, destination:8}); homelogo_nav.click({location:2})">
					<span class="-img _glyph">Stack Overflow</span>
				</a>



			<ol class="s-navigation fw-nowrap" role="presentation">

					<li class="md:d-none">
						<a href="https://stackoverflow.co/" class="s-navigation--item js-gps-track"
				   data-gps-track="top_nav.products.click({location:2, destination:7})"
				   data-ga="[&quot;top navigation&quot;,&quot;about menu click&quot;,null,null,null]">About</a>
					</li>

				<li>
					<button
						class="s-navigation--item js-gps-track"
						type="button"
						aria-controls="products-popover"
						aria-expanded="false"
						data-controller="s-popover"
						data-action="s-popover#toggle"
						data-s-popover-toggle-class="is-selected"
						data-gps-track="top_nav.products.click({location:2, destination:1})"
						data-ga="[&quot;top navigation&quot;,&quot;products menu click&quot;,null,null,null]">
							Products
					</button>
				</li>

                    <li class="md:d-none">
                        <a href="https://stackoverflow.co/teams/ai/?utm_medium=referral&amp;utm_source=stackoverflow-community&amp;utm_campaign=top-nav-bar&amp;utm_content=overflowai" class="s-navigation--item js-gps-track"
                        data-gps-track="top_nav.products.click({location:2, destination:10})"
                        data-ga="[&quot;top navigation&quot;,&quot;learn more - overflowai&quot;,null,null,null]">OverflowAI</a>
                    </li>

			</ol>
			<div class="s-popover ws2 mtn2 p0"
			 id="products-popover"
			 role="menu"
			 aria-hidden="true">
				<div class="s-popover--arrow"></div>
				<ol class="list-reset s-anchors s-anchors__inherit">
					<li class="m6">
						<a href="https://stackoverflow.co/teams/?utm_medium=referral&utm_source=stackoverflow-community&utm_campaign=top-nav&utm_content=stack-overflow-for-teams" class="bar-sm p6 d-block h:bg-black-225 js-gps-track"
					   data-gps-track="top_nav.products.click({location:2, destination:3})"
					   data-ga="[&quot;top navigation&quot;,&quot;teams submenu click&quot;,null,null,null]">
							<span class="fs-body1 d-block">Stack Overflow for Teams</span>
							<span class="fs-caption d-block fc-black-400">Where developers &amp; technologists share private knowledge with coworkers</span>
						</a>
					</li>
					<li class="m6">
						<a href="https://stackoverflow.co/advertising/?utm_medium=referral&utm_source=stackoverflow-community&utm_campaign=top-nav&utm_content=stack-overflow-advertising" class="bar-sm p6 d-block h:bg-black-225 js-gps-track"
					   data-gps-track="top_nav.products.click({location:2, destination:6})"
					   data-ga="[&quot;top navigation&quot;,&quot;advertising submenu click&quot;,null,null,null]">
							<span class="fs-body1 d-block">Advertising &amp; Talent</span>
							<span class="fs-caption d-block fc-black-400">Reach devs &amp; technologists worldwide about your product, service or employer brand</span>
						</a>
					</li>
					<li class="bt bc-black-200 pt6 px6 bbr-md">
						<a href="https://stackoverflow.co/teams/ai/?utm_medium=referral&utm_source=stackoverflow-community&utm_campaign=top-nav&utm_content=overflow-ai" class="bar-sm p6 d-block h:bg-black-225 js-gps-track"
					   data-gps-track="top_nav.products.click({location:2, destination:10})"
					   data-ga="[&quot;top navigation&quot;,&quot;overflowai submenu click&quot;,null,null,null]">
						 	<span class="fs-body1 d-block">OverflowAI</span>
							<span class="fs-caption d-block fc-black-400">GenAI features for Teams</span>
						 </a>
					</li>
					<li class="pb6 px6 bbr-md">
						<a href="https://stackoverflow.co/api-solutions/?utm_medium=referral&utm_source=stackoverflow-community&utm_campaign=top-nav&utm_content=overflow-api" class="bar-sm p6 d-block h:bg-black-225 js-gps-track"
					   data-gps-track="top_nav.products.click({location:2, destination:11})"
					   data-ga="[&quot;top navigation&quot;,&quot;overflowapi submenu click&quot;,null,null,null]">
						 	<span class="fs-body1 d-block">OverflowAPI</span>
							<span class="fs-caption d-block fc-black-400">Train &amp; fine-tune LLMs</span>
						 </a>
					</li>
					<li class="bt bc-black-200 py6 px6 bbr-md">
						<a href="https://stackoverflow.co/labs/?utm_medium=referral&utm_source=stackoverflow-community&utm_campaign=top-nav&utm_content=labs" class="bar-sm p6 d-block h:bg-black-225 js-gps-track"
					   data-gps-track="top_nav.products.click({location:2, destination:12})"
					   data-ga="[&quot;top navigation&quot;,&quot;labs submenu click&quot;,null,null,null]">
						 	<span class="fs-body1 d-block">Labs</span>
							<span class="fs-caption d-block fc-black-400">The future of collective knowledge sharing</span>
						 </a>
					</li>
					<li class="bg-black-100 bt bc-black-200 py6 px6 bbr-md">
						<a href="https://stackoverflow.co/?utm_medium=referral&utm_source=stackoverflow-community&utm_campaign=top-nav&utm_content=about-the-company" class="fc-black-400 d-block py6 px6 h:fc-black-600"
					   data-ga="[&quot;top navigation&quot;,&quot;about submenu click&quot;,null,null,null]">About the company</a>

						<a href="https://stackoverflow.blog/?utm_medium=referral&utm_source=stackoverflow-community&utm_campaign=top-nav&utm_content=blog" class="fc-black-400 d-block py6 px6 h:fc-black-600"
					   data-ga="[&quot;top navigation&quot;,&quot;blog submenu click&quot;,null,null,null]">Visit the blog</a>
					</li>
				</ol>
			</div>


		        <form id="search" role="search" action=/search class="s-topbar--searchbar js-searchbar " autocomplete="off">
                        <div class="s-topbar--searchbar--input-group">
                            <input name="q"
                                   type="text"
                                   role="combobox"
                                   placeholder="Search&#x2026;"
                                   value=""
                                   autocomplete="off"
                                   maxlength="240"
                                   class="s-input s-input__search js-search-field wmn1 "
                                   aria-label="Search"
                                   aria-controls="top-search" 
                                   data-controller="s-popover"
                                   data-action="focus->s-popover#show"
                                   data-s-popover-placement="bottom-start" />
                            <svg aria-hidden="true" class="s-input-icon s-input-icon__search svg-icon iconSearch" width="18" height="18"  viewBox="0 0 18 18"><path  d="m18 16.5-5.14-5.18h-.35a7 7 0 1 0-1.19 1.19v.35L16.5 18zM12 7A5 5 0 1 1 2 7a5 5 0 0 1 10 0"/></svg>
                            <div class="s-popover p0 wmx100 wmn4 sm:wmn-initial js-top-search-popover" id="top-search" role="menu">
    <div class="s-popover--arrow"></div>
    <div class="s-popover--content">
        <div class="js-spinner p24 d-flex ai-center jc-center d-none">
            <div class="s-spinner s-spinner__sm fc-orange-400">
                <div class="v-visible-sr">Loading&#x2026;</div>
            </div>
        </div>

        <span class="v-visible-sr js-screen-reader-info"></span>
        <div class="js-ac-results overflow-y-auto hmx3 d-none"></div>

        <div class="js-search-hints" aria-describedby="Tips for searching"></div>
    </div>
</div>
                        </div>
                </form>
		

<nav class="h100 ml-auto overflow-x-auto pr12" aria-label="Topbar">
    <ol class="s-topbar--content" role="menubar">
    
    
    
        <li class="js-topbar-dialog-corral" role="presentation">
                

    <div class="topbar-dialog siteSwitcher-dialog dno" role="menu">
        <div class="header fw-wrap">
            <h3 class="flex--item">
                <a href="https://stackoverflow.com">current community</a>
            </h3>
            <div class="flex--item fl1">
                <div class="ai-center d-flex jc-end">
                    <button
                        class="js-close-button s-btn s-btn__muted p0 ml8 d-none sm:d-block"
                        type="button"
                        aria-label="Close"
                    >
                        <svg aria-hidden="true" class="svg-icon iconClear" width="18" height="18"  viewBox="0 0 18 18"><path  d="M15 4.41 13.59 3 9 7.59 4.41 3 3 4.41 7.59 9 3 13.59 4.41 15 9 10.41 13.59 15 15 13.59 10.41 9z"/></svg>
                    </button>
                </div>
            </div>
        </div>
        <div class="modal-content bg-blue-200 current-site-container">
            <ul class="current-site">
                    <li class="d-flex">
                            <div class="fl1">
                <a href="https://stackoverflow.com"  
       class="current-site-link d-flex gx8 site-link js-gps-track"
       data-id="1"
       data-gps-track="site_switcher.click({ item_type:3 })">
        <div class="favicon favicon-stackoverflow site-icon flex--item" title="Stack Overflow"></div>
        <span class="flex--item fl1">
            Stack Overflow
        </span>
    </a>

    </div>
    <div class="related-links">
            <a href="https://stackoverflow.com/help" class="js-gps-track" data-gps-track="site_switcher.click({ item_type:14 })">help</a>
            <a href="https://chat.stackoverflow.com/?tab=site&amp;host=stackoverflow.com" class="js-gps-track" data-gps-track="site_switcher.click({ item_type:6 })">chat</a>
    </div>

                    </li>
                    <li class="related-site d-flex">
                            <div class="L-shaped-icon-container">
        <span class="L-shaped-icon"></span>
    </div>

                            <a href="https://meta.stackoverflow.com"  
       class="s-block-link px16 d-flex gx8 site-link js-gps-track"
       data-id="552"
       data-gps-track="site.switch({ target_site:552, item_type:3 }),site_switcher.click({ item_type:4 })">
        <div class="favicon favicon-stackoverflowmeta site-icon flex--item" title="Meta Stack Overflow"></div>
        <span class="flex--item fl1">
            Meta Stack Overflow
        </span>
    </a>

                    </li>
            </ul>
        </div>

        <div class="header" id="your-communities-header">
            <h3>
your communities            </h3>

        </div>
        <div class="modal-content" id="your-communities-section">

                <div class="call-to-login">
<a href="https://stackoverflow.com/users/signup?ssrc=site_switcher&amp;returnurl=https%3a%2f%2fstackoverflow.com%2fquestions%2f35302978%2fhow-to-get-current-value-of-androids-proximity-sensor" class="login-link js-gps-track" data-gps-track="site_switcher.click({ item_type:10 })">Sign up</a> or <a href="https://stackoverflow.com/users/login?ssrc=site_switcher&amp;returnurl=https%3a%2f%2fstackoverflow.com%2fquestions%2f35302978%2fhow-to-get-current-value-of-androids-proximity-sensor" class="login-link js-gps-track" data-gps-track="site_switcher.click({ item_type:11 })">log in</a> to customize your list.                </div>
        </div>

        <div class="header">
            <h3><a href="https://stackexchange.com/sites">more stack exchange communities</a>
            </h3>
            <a href="https://stackoverflow.blog" class="float-right">company blog</a>
        </div>
        <div class="modal-content">
                <div class="child-content"></div>
        </div>        
    </div>

        </li>
    
            <li role="none"><button class="s-topbar--item s-btn s-btn__icon s-btn__muted d-none sm:d-inline-flex js-searchbar-trigger" role="menuitem" aria-label="Search" aria-haspopup="true" aria-controls="search" title="Click to show search"><svg aria-hidden="true" class="svg-icon iconSearch" width="18" height="18"  viewBox="0 0 18 18"><path  d="m18 16.5-5.14-5.18h-.35a7 7 0 1 0-1.19 1.19v.35L16.5 18zM12 7A5 5 0 1 1 2 7a5 5 0 0 1 10 0"/></svg></button></li>
                        <li role="none">
                            <a href="https://stackoverflow.com/users/login?ssrc=head&returnurl=https%3a%2f%2fstackoverflow.com%2fquestions%2f35302978%2fhow-to-get-current-value-of-androids-proximity-sensor" class="s-topbar--item s-topbar--item__unset s-btn s-btn__outlined ws-nowrap js-gps-track" role="menuitem" rel="nofollow"
                               data-gps-track="login.click" data-ga="[&quot;top navigation&quot;,&quot;login button click&quot;,null,null,null]">Log in</a>
                        </li>
                        <li role="none"><a href="https://stackoverflow.com/users/signup?ssrc=head&returnurl=https%3a%2f%2fstackoverflow.com%2fquestions%2f35302978%2fhow-to-get-current-value-of-androids-proximity-sensor" class="s-topbar--item s-topbar--item__unset ml4 s-btn s-btn__filled ws-nowrap js-signup-button js-gps-track" role="menuitem" rel="nofollow" data-gps-track="signup.topbar.click" data-ga="[&quot;sign up&quot;,&quot;Sign Up Navigation&quot;,&quot;Header&quot;,null,null]">Sign up</a></li>
    </ol>
</nav>


	</div>
</header>

	<script>
		StackExchange.ready(function () { StackExchange.topbar.init(); });
		StackExchange.scrollPadding.setPaddingTop(50, 10); 
	</script>





    <div class="container">
                


    <div id="homepage-wizard-container"></div>
<script type="application/json" data-role="module-args" data-module-name="islands/homepage-wizard/index.mod">{"ContainerElementId":"homepage-wizard-container","FKey":"3263e220c9fc053cefe5230c13d734e7914d13795116a71a9d8e74c9e9fe345a","Tags":["javascript","python","java","c#","php","android","html","jquery","c++","css","ios","sql","mysql","r","reactjs","node.js","arrays","c","asp.net","json","python-3.x",".net","ruby-on-rails","sql-server","swift","django","angular","objective-c","excel","pandas","angularjs","regex","typescript","ruby","linux","ajax","iphone","vba","xml","laravel","spring","asp.net-mvc","database","wordpress","string","flutter","postgresql","mongodb","wpf","windows","amazon-web-services","xcode","bash","git","oracle-database","spring-boot","dataframe","firebase","azure","list","multithreading","vb.net","docker","react-native","eclipse","algorithm","powershell","macos","visual-studio","numpy","image","forms","scala","function","vue.js","twitter-bootstrap","performance","selenium","winforms","kotlin","loops","express","dart","hibernate","sqlite","matlab","python-2.7","shell","rest","apache","api","entity-framework","android-studio","csv","maven","linq","qt","dictionary","unit-testing","facebook","asp.net-core","tensorflow","apache-spark","file","swing","class","unity-game-engine","sorting","date","authentication","symfony","go","opencv","t-sql",".htaccess","matplotlib","google-chrome","for-loop","datetime","codeigniter","http","perl","validation","sockets","google-maps","object","uitableview","xaml","oop","if-statement","visual-studio-code","cordova","ubuntu","web-services","email","android-layout","github","elasticsearch","spring-mvc","kubernetes","selenium-webdriver","ms-access","user-interface","parsing","ggplot2","pointers","c++11","machine-learning","security","google-sheets","flask","ruby-on-rails-3","nginx","google-apps-script","templates","variables","exception","sql-server-2008","gradle","debugging","tkinter","listview","delphi","jpa","asynchronous","pdf","web-scraping","jsp","haskell","ssl","amazon-s3","google-cloud-platform","jenkins","xamarin","testing","wcf","npm","batch-file","generics","ionic-framework","network-programming","unix","recursion","google-app-engine","mongoose","visual-studio-2010",".net-core","android-fragments","assembly","animation","math","session","next.js","hadoop","svg","intellij-idea","curl","django-models","join","laravel-5","heroku","url","winapi","http-redirect","tomcat","rust","google-cloud-firestore","web","inheritance","webpack","keras","image-processing","asp.net-mvc-4","gcc","logging","dom","matrix","pyspark","actionscript-3","swiftui","button","post","firebase-realtime-database","optimization","jquery-ui","cocoa","iis","xpath","d3.js","firefox","internet-explorer","javafx","xslt","caching","select","asp.net-mvc-3","opengl","events","asp.net-web-api","plot","dplyr","magento","encryption","search","stored-procedures","amazon-ec2","ruby-on-rails-4","memory","audio","canvas","multidimensional-array","jsf","random","redux","cookies","vector","facebook-graph-api","input","flash","xamarin.forms","arraylist","indexing","ipad","cocoa-touch","data-structures","video","model-view-controller","apache-kafka","serialization","jdbc","woocommerce","routes","razor","awk","servlets","mod-rewrite","azure-devops","beautifulsoup","iframe","docker-compose","filter","excel-formula","aws-lambda","design-patterns","django-rest-framework","text","visual-c++","cakephp","mobile","android-intent","react-hooks","struct","methods","groovy","mvvm","ssh","lambda","checkbox","ecmascript-6","google-chrome-extension","time","grails","installation","sharepoint","shiny","spring-security","cmake","jakarta-ee","android-recyclerview","core-data","plsql","meteor","types","android-activity","sed","bootstrap-4","websocket","activerecord","graph","replace","scikit-learn","file-upload","group-by","vim","junit","boost","deep-learning","import","sass","memory-management","error-handling","async-await","eloquent","dynamic","soap","silverlight","charts","dependency-injection","apache-spark-sql","layout","deployment","browser","gridview","svn","while-loop","google-bigquery","vuejs2","ffmpeg","dll","highcharts","view","foreach","c#-4.0","plugins","redis","makefile","reporting-services","jupyter-notebook","server","merge","https","unicode","reflection","google-maps-api-3","twitter","extjs","oauth-2.0","axios","pytorch","terminal","pip","split","mysqli","django-views","cmd","encoding","netbeans","database-design","collections","hash","automation","ember.js","data-binding","build","tcp","pdo","sqlalchemy","apache-flex","command-line","printing","spring-data-jpa","entity-framework-core","concurrency","java-8","react-redux","jestjs","service","html-table","neo4j","ansible","lua","parameters","material-ui","visual-studio-2012","module","enums","promise","flexbox","outlook","webview","firebase-authentication","web-applications","uwp","jquery-mobile","utf-8","datatable","python-requests","drop-down-menu","scroll","colors","parallel-processing","hive","tfs","scipy","count","syntax","ms-word","twitter-bootstrap-3","ssis","google-analytics","fonts","three.js","graphql","constructor","file-io","rxjs","paypal","powerbi","discord","cassandra","socket.io","graphics","gwt","compiler-errors","nlp","react-router","solr","url-rewriting","backbone.js","datatables","memory-leaks","datagridview","oauth","oracle11g","drupal","zend-framework","neural-network","terraform","knockout.js","django-forms","interface","triggers","google-api","casting","angular-material","linked-list","jmeter","proxy","path","timer","django-templates","directory","orm","parse-platform","visual-studio-2015","arduino","cron","windows-phone-7","push-notification","conditional-statements","primefaces","functional-programming","pagination","model","jar","xamarin.android","hyperlink","uiview","visual-studio-2013","vbscript","gitlab","google-cloud-functions","azure-active-directory","download","jwt","swift3","sql-server-2005","process","configuration","rspec","properties","callback","pygame","combobox","windows-phone-8","safari","permissions","linux-kernel","scrapy","raspberry-pi","scripting","emacs","clojure","scope","io","x86","mongodb-query","compilation","angularjs-directive","nhibernate","responsive-design","request","bluetooth","dns","3d","binding","reference","discord.js","architecture","playframework","version-control","pyqt","doctrine-orm","expo","package","azure-functions","pycharm","get","sql-server-2012","rubygems","f#","autocomplete","datepicker","openssl","kendo-ui","tree","jackson","controller","yii","xamarin.ios","grep","nested","static","statistics","datagrid","dockerfile","active-directory","transactions","null","uiviewcontroller","phpmyadmin","webforms","discord.py","notifications","sas","computer-vision","duplicates","youtube","mocking","nullpointerexception","menu","yaml","bitmap","sum","asp.net-mvc-5","electron","visual-studio-2008","jsf-2","yii2","time-series","android-listview","stl","stream","css-selectors","floating-point","ant","cryptography","character-encoding","hashmap","blazor","sdk","msbuild","selenium-chromedriver","google-drive-api","jboss","asp.net-core-mvc","frontend","joomla","devise","anaconda","navigation","cors","background","camera","binary","pyqt5","multiprocessing","linq-to-sql","cuda","iterator","onclick","ios7","mariadb","plotly","rabbitmq","android-asynctask","laravel-4","tabs","insert","uicollectionview","amazon-dynamodb","environment-variables","microsoft-graph-api","linker","android-jetpack-compose","console","xsd","upload","coldfusion","ftp","continuous-integration","textview","opengl-es","operating-system","localization","xml-parsing","mockito","formatting","macros","kivy","json.net","vuejs3","type-conversion","data.table","timestamp","calendar","integer","segmentation-fault","android-ndk","drag-and-drop","prolog","char","crash","jasmine","automated-tests","dependencies","itext","android-gradle-plugin","header","firebase-cloud-messaging","geometry","sprite-kit","mfc","fortran","nosql","attributes","nuxt.js","format","nestjs","jquery-plugins","odoo","db2","leaflet","jenkins-pipeline","event-handling","postman","flutter-layout","azure-pipelines","annotations","julia","keyboard","textbox","arm","visual-studio-2017","gulp","libgdx","xampp","synchronization","crystal-reports","stripe-payments","dom-events","timezone","azure-web-app-service","swagger","android-emulator","sequelize.js","wso2","uikit","uiscrollview","aggregation-framework","namespaces","jvm","chart.js","com","webdriver","geolocation","centos","subprocess","google-sheets-formula","widget","html5-canvas","dialog","garbage-collection","numbers","concatenation","sql-update","mapreduce","qml","windows-10","set","ionic2","smtp","tuples","snowflake-cloud-data-platform","modal-dialog","rotation","android-edittext","http-headers","spring-data","doctrine","radio-button","grid","nuget","sonarqube","java-stream","lucene","xmlhttprequest","internationalization","listbox","components","switch-statement","initialization","apache-camel","google-play","boolean","serial-port","ldap","ios5","youtube-api","return","eclipse-plugin","pivot","latex","gdb","frameworks","tags","containers","dataset","asp-classic","foreign-keys","subquery","label","uinavigationcontroller","copy","delegates","google-cloud-storage","github-actions","struts2","migration","base64","protractor","c++17","sql-server-2008-r2","queue","find","uibutton","arguments","composer-php","append","embedded","jaxb","zip","stack","cucumber","autolayout","ide","popup","entity-framework-6","iteration","windows-7","r-markdown","vb6","gmail","ssl-certificate","airflow","jqgrid","hover","android-viewpager","passwords","udp"],"TriggerEvent":"homepageWizardShow","OauthInPopup":true,"ReturnUrl":"https://stackoverflow.com","ReturnUrlForPopup":"https://stackoverflow.com/users/after-signup/oauth-only"}</script><script defer src="https://cdn.sstatic.net/Js/webpack-chunks/svelte.en.js?v=150134e89426"></script><script defer src="https://cdn.sstatic.net/Js/webpack-chunks/stacks-svelte.en.js?v=72feec5d5528"></script><script defer src="https://cdn.sstatic.net/Js/webpack-chunks/3397.en.js?v=ecde4075784a"></script><script defer src="https://cdn.sstatic.net/Js/webpack-chunks/1315.en.js?v=d971ebf7a8e2"></script><script defer src="https://cdn.sstatic.net/Js/webpack-chunks/7224.en.js?v=8ca862d5f302"></script><script defer src="https://cdn.sstatic.net/Js/webpack-chunks/4537.en.js?v=e6769247457b"></script><script defer src="https://cdn.sstatic.net/Js/islands/homepage-wizard.en.js?v=564cf5bf9c49"></script>
<div id="left-sidebar" data-is-here-when="md lg" class="left-sidebar js-pinned-left-sidebar ps-relative">
    <div class="left-sidebar--sticky-container js-sticky-leftnav">
        <nav aria-label="Primary">
            <ol class="nav-links">
                <li>
                    <ol class="nav-links">
                        

<li class="ps-relative"  aria-current="false">


    <a
       href="/"
       class="s-block-link pl8 js-homepage-wizard-link js-gps-track nav-links--link -link__with-icon"
       
       data-gps-track="top_nav.click({is_current: false, location:2, destination:8,  has_activity_notification:False});home_nav.click({location:2})"
       aria-controls=""
       data-controller=" "
       data-s-popover-placement="right"
       aria-current="false"
       data-s-popover-auto-show="true" data-s-popover-hide-on-outside-click="never"
    >
        <div class="d-flex ai-center">
<svg aria-hidden="true" class="svg-icon iconHome" width="18" height="18"  viewBox="0 0 18 18"><path  d="M15 10v5a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-5H0l9-9 9 9zm-8 1v6h4v-6z"/></svg>                <span class="-link--channel-name pl6">Home</span>

        </div>
    </a>
</li>



                        

<li class="ps-relative  youarehere"  aria-current="true">


    <a id="nav-questions"
       href="/questions"
       class="s-block-link pl8 js-gps-track nav-links--link -link__with-icon"
       
       data-gps-track="top_nav.click({is_current: true, location:2, destination:1,  has_activity_notification:False})"
       aria-controls=""
       data-controller=" "
       data-s-popover-placement="right"
       aria-current="false"
       data-s-popover-auto-show="true" data-s-popover-hide-on-outside-click="never"
    >
        <div class="d-flex ai-center">
<svg aria-hidden="true" class="svg-icon iconQuestion" width="18" height="18"  viewBox="0 0 18 18"><path  d="m4 15-3 3V4c0-1.1.9-2 2-2h12c1.09 0 2 .91 2 2v9c0 1.09-.91 2-2 2zm7.75-3.97c.72-.83.98-1.86.98-2.94 0-1.65-.7-3.22-2.3-3.83a4.4 4.4 0 0 0-3.02 0 3.8 3.8 0 0 0-2.32 3.83q0 1.93 1.03 3a3.8 3.8 0 0 0 2.85 1.07q.94 0 1.71-.34.97.66 1.06.7.34.2.7.3l.59-1.13a5 5 0 0 1-1.28-.66m-1.27-.9a5 5 0 0 0-1.5-.8l-.45.9q.5.18.98.5-.3.1-.65.11-.92 0-1.52-.68c-.86-1-.86-3.12 0-4.11.8-.9 2.35-.9 3.15 0 .9 1.01.86 3.03-.01 4.08"/></svg>                <span class="-link--channel-name pl6">Questions</span>

        </div>
    </a>
</li>






                        

<li class="ps-relative"  aria-current="false">


    <a
       href="/tags"
       class="s-block-link pl8 js-gps-track nav-links--link -link__with-icon"
       
       data-gps-track="top_nav.click({is_current: false, location:2, destination:2,  has_activity_notification:False})"
       aria-controls=""
       data-controller=" "
       data-s-popover-placement="right"
       aria-current="false"
       data-s-popover-auto-show="true" data-s-popover-hide-on-outside-click="never"
    >
        <div class="d-flex ai-center">
<svg aria-hidden="true" class="svg-icon iconTags" width="18" height="18"  viewBox="0 0 18 18"><path  d="M9.24 1a3 3 0 0 0-2.12.88l-5.7 5.7a2 2 0 0 0-.38 2.31 3 3 0 0 1 .67-1.01l6-6A3 3 0 0 1 9.83 2H14a3 3 0 0 1 .79.1A2 2 0 0 0 13 1z" opacity=".4"/><path  d="M9.83 3a2 2 0 0 0-1.42.59l-6 6a2 2 0 0 0 0 2.82L6.6 16.6a2 2 0 0 0 2.82 0l6-6A2 2 0 0 0 16 9.17V5a2 2 0 0 0-2-2zM12 9a2 2 0 1 1 0-4 2 2 0 0 1 0 4"/></svg>                <span class="-link--channel-name pl6">Tags</span>

        </div>
    </a>
</li>


                        
                        <li class="pb24"></li>


                        

<li class="ps-relative"  aria-current="false">


    <a id="nav-users"
       href="/users"
       class="s-block-link pl8 js-gps-track nav-links--link -link__with-icon"
       
       data-gps-track="top_nav.click({is_current: false, location:2, destination:3,  has_activity_notification:False})"
       aria-controls=""
       data-controller=" "
       data-s-popover-placement="right"
       aria-current="false"
       data-s-popover-auto-show="true" data-s-popover-hide-on-outside-click="never"
    >
        <div class="d-flex ai-center">
<svg aria-hidden="true" class="svg-icon iconPeople" width="18" height="18"  viewBox="0 0 18 18"><path  d="M17 14c0 .44-.45 1-1 1H9a1 1 0 0 1-1-1H2c-.54 0-1-.56-1-1 0-2.63 3-4 3-4s.23-.4 0-1c-.84-.62-1.06-.59-1-3s1.37-3 2.5-3 2.44.58 2.5 3-.16 2.38-1 3c-.23.59 0 1 0 1s1.55.71 2.42 2.09c.78-.72 1.58-1.1 1.58-1.1s.23-.4 0-1c-.84-.61-1.06-.58-1-3s1.37-3 2.5-3 2.44.59 2.5 3c.05 2.42-.16 2.39-1 3-.23.6 0 1 0 1s3 1.38 3 4"/></svg>                <span class="-link--channel-name pl6">Users</span>

        </div>
    </a>
</li>


                            

<li class="ps-relative"  aria-current="false">


    <a id="nav-companies"
       href="https://stackoverflow.com/jobs/companies?so_medium=stackoverflow&amp;so_source=SiteNav"
       class="s-block-link pl8 js-gps-track nav-links--link -link__with-icon"
       
       data-gps-track="top_nav.click({is_current: false, location:2, destination:12,  has_activity_notification:False})"
       aria-controls=""
       data-controller=" "
       data-s-popover-placement="right"
       aria-current="false"
       data-s-popover-auto-show="true" data-s-popover-hide-on-outside-click="never"
    >
        <div class="d-flex ai-center">
<svg aria-hidden="true" class="svg-icon iconIndustry" width="18" height="18"  viewBox="0 0 18 18"><path  d="M10 16v-4H8v4H2V4c0-1.1.9-2 2-2h6c1.09 0 2 .91 2 2v2h2c1.09 0 2 .91 2 2v8zM4 4v2h2V4zm0 4v2h2V8zm4-4v2h2V4zm0 4v2h2V8zm-4 4v2h2v-2zm8 0v2h2v-2zm0-4v2h2V8z"/></svg>                <span class="-link--channel-name pl6">Companies</span>

        </div>
    </a>
</li>




        <li class="ml8 mt32 mb8">
            <a href="javascript:void(0)"
               class="s-link s-link d-flex fl-grow1 fc-black-400 h:fc-black-600 fs-fine"
               role="button"
               aria-controls="popover-labs-left-nav"
               data-controller="s-popover"
               data-action="s-popover#toggle"
               data-s-popover-placement="top"
               data-s-popover-toggle-class="is-selected"
            >
                <div class="flex--item fl-grow1 tt-uppercase fc-black-600 fw-bold">Labs</div>
                <div class="flex--item px12">
                    <svg aria-hidden="true" class="svg-icon iconInfoSm" width="14" height="14"  viewBox="0 0 14 14"><path  d="M7 1a6 6 0 1 1 0 12A6 6 0 0 1 7 1m1 10V6H6v5zm0-6V3H6v2z"/></svg>
                </div>
            </a>
        </li>
        

<li class="ps-relative"  aria-current="false">


    <a id="nav-labs-jobs"
       href="/jobs?source=so-left-nav"
       class="s-block-link pl8 ai-center js-disable-jobs-new-link js-gps-track nav-links--link -link__with-icon"
       
       data-gps-track="top_nav.click({is_current: false, location:2, destination:26,  has_activity_notification:False});jobs.click({destination:JobsFakeDoor, is_registered:False, rep_bucket:new, origin:Stack Overflow})"
       aria-controls=""
       data-controller=" "
       data-s-popover-placement="right"
       aria-current="false"
       data-s-popover-auto-show="true" data-s-popover-hide-on-outside-click="never"
    >
        <div class="d-flex ai-center">
<svg aria-hidden="true" class="svg-icon iconBriefcase" width="18" height="18"  viewBox="0 0 18 18"><path  d="M5 4a1 1 0 0 1 1-1h6a1 1 0 0 1 1 1v1h1a2 2 0 0 1 2 2v6a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V7c0-1.1.9-2 2-2h1zm7 0H6v1h6z"/></svg>                <span class="-link--channel-name pl6">Jobs</span>

        </div>
    </a>
</li>


                

<li class="ps-relative"  aria-current="false">


    <a id="nav-labs-discussions"
       href="/beta/discussions"
       class="s-block-link pl8 ai-center js-gps-track nav-links--link -link__with-icon"
       
       data-gps-track="top_nav.click({is_current: false, location:2, destination:24,  has_activity_notification:False})"
       aria-controls=""
       data-controller=" "
       data-s-popover-placement="right"
       aria-current="false"
       data-s-popover-auto-show="true" data-s-popover-hide-on-outside-click="never"
    >
        <div class="d-flex ai-center">
<svg aria-hidden="true" class="w16 svg-icon iconMessage" width="18" height="18"  viewBox="0 0 18 18"><path  d="M5 7a1 1 0 0 1 1-1h6a1 1 0 1 1 0 2H6a1 1 0 0 1-1-1m1 2a1 1 0 1 0 0 2h4a1 1 0 1 0 0-2zm-5 9V4c0-1.1.9-2 2-2h12c1.09 0 2 .91 2 2v9c0 1.09-.91 2-2 2H4.5zm2.76-5h11.23v-.01H15V4H3v9.65z"/></svg>                <span class="-link--channel-name pl6">Discussions</span>

        </div>
    </a>
</li>



                            <li class="ml8 mt32 mb4">
                                <div class="d-flex jc-space-between ai-center">
                                    <a
                                        class="s-link d-flex fl-grow1 fc-black-400 h:fc-black-600 fs-fine"
                                        href="javascript:void(0)"
                                        role="button"
                                        aria-controls="popover-discover-collectives"
                                        data-controller="s-popover"
                                        data-action="s-popover#toggle"
                                        data-s-popover-placement="top"
                                        data-s-popover-toggle-class="is-selected"
                                        data-gps-track="top_nav.click({is_current:false, location:2, destination:17})"
                                    >
                                        <div class="flex--item fl-grow1 tt-uppercase fc-black-600 fw-bold">Collectives</div>
                                        <div class="flex--item px12 js-collectives-navcta-toggle">
                                            <svg aria-hidden="true" class="svg-icon iconPlusSm" width="14" height="14"  viewBox="0 0 14 14"><path  d="M8 2H6v4H2v2h4v4h2V8h4V6H8z"/></svg>
                                        </div>
                                    </a>
                                </div>

                            </li>
                                <li class="ps-relative js-collectives-navcta-toggle">
                                    <p class="fs-fine pr8 pl8 pt4 fc-black-400">
                                        Communities for your favorite technologies.  <a href="/collectives-all" class="s-link s-link__grayscale s-link__underlined fw-bold">Explore all Collectives</a>
                                    </p>
                                </li>

                        
                    </ol>
                </li>
                
                

        

<li class="js-freemium-cta ps-relative mt32 mb8">


    <div class="fs-fine tt-uppercase fc-black-600 fw-bold ml8 mt16 mb8">Teams</div>

    <div class="px12 pt12 pb4 mb12 fc-medium overflow-hidden">        
        <img class="wmx100 mx-auto mb12 h-auto d-block" width="151" height="24" src="https://cdn.sstatic.net/Img/teams/teams-promo.svg?v=e507948b81bf" alt="">
        <p class="fs-fine">
            Ask questions, find answers and collaborate at work with Stack Overflow for Teams.
        </p>
        <a href="https://stackoverflowteams.com/teams/create/free/?utm_medium=referral&utm_source=stackoverflow-community&utm_campaign=side-bar&utm_content=explore-teams"
           class="w100 s-btn s-btn__filled s-btn__xs bg-orange-400 h:bg-orange-500 js-gps-track pt8 pr7 pb6 pl7"
           data-gps-track="teams.create.left-sidenav.click({ Action: 6 })"
           data-ga="[&quot;teams left navigation - anonymous&quot;,&quot;left nav free cta&quot;,&quot;stackoverflow.com/teams/create/free&quot;,null,null]">Try Teams for free</a>
        <a href="https://stackoverflow.co/teams/?utm_medium=referral&utm_source=stackoverflow-community&utm_campaign=side-bar&utm_content=explore-teams"
           class="w100 s-btn s-btn__muted s-btn__xs mt1 js-gps-track"
           data-gps-track="teams.create.left-sidenav.click({ Action: 5 })"
           data-ga="[&quot;teams left navigation - anonymous&quot;,&quot;left nav free cta&quot;,&quot;stackoverflow.com/teams&quot;,null,null]">Explore Teams</a>
    </div>
</li>


    <li class="d-flex ai-center jc-space-between ml8 mt32 mb8 js-create-team-cta d-none">

        <a href="javascript:void(0)"
            class="s-link d-flex fl-grow1 fc-black-400 h:fc-black-600 fs-fine js-gps-track"
            role="button"
            aria-controls="popover-teams-create-cta"
            data-controller="s-popover"
            data-action="s-popover#toggle"
            data-s-popover-placement="bottom-start"
            data-s-popover-toggle-class="is-selected"
            data-gps-track="teams.create.left-sidenav.click({ Action: ShowInfo })"
            data-ga="[&quot;teams left navigation - anonymous&quot;,&quot;left nav show teams info&quot;,null,null,null]"
         >
            <div class="flex--item fl-grow1 fc-black-600 fw-bold tt-uppercase">Teams</div>
            <div class="flex--item px12">
                <svg aria-hidden="true" class="svg-icon iconPlusSm" width="14" height="14"  viewBox="0 0 14 14"><path  d="M8 2H6v4H2v2h4v4h2V8h4V6H8z"/></svg>
            </div>
        </a>
    </li>
    <li class="ps-relative js-create-team-cta d-none">
        <p class="fs-fine pr8 pl8 pb4 fc-black-400">
            Ask questions, find answers and collaborate at work with Stack Overflow for Teams.
            <a href="https://stackoverflow.co/teams/?utm_medium=referral&utm_source=stackoverflow-community&utm_campaign=side-bar&utm_content=explore-teams-compact" class="s-link s-link__grayscale s-link__underlined fw-bold">Explore Teams</a>
        </p>
    </li> 

            </ol>
        </nav>
    </div>


        <div class="s-popover ws2" id="popover-discover-collectives" role="menu">
            <div class="s-popover--arrow"></div>
            <div>
                <svg aria-hidden="true" class="fc-orange-400 float-right ml24 svg-spot spotCollective" width="48" height="48"  viewBox="0 0 48 48"><path  d="M25.5 7a2.5 2.5 0 1 0 0-5 2.5 2.5 0 0 0 0 5M14 18.25c0-.69.56-1.25 1.25-1.25h22.5c.69 0 1.25.56 1.25 1.25V37.5a1 1 0 0 1-1.6.8l-4.07-3.05a1.3 1.3 0 0 0-.75-.25H15.25c-.69 0-1.25-.56-1.25-1.25zM7 24.5a2.5 2.5 0 1 1-5 0 2.5 2.5 0 0 1 5 0M25.5 48a2.5 2.5 0 1 0 0-5 2.5 2.5 0 0 0 0 5M48 24.5a2.5 2.5 0 1 1-5 0 2.5 2.5 0 0 1 5 0" opacity=".2"/><path  d="M21 3.5a3.5 3.5 0 1 1 7 0 3.5 3.5 0 0 1-7 0M24.5 2a1.5 1.5 0 1 0 0 3 1.5 1.5 0 0 0 0-3M0 23.5a3.5 3.5 0 1 1 7 0 3.5 3.5 0 0 1-7 0M3.5 22a1.5 1.5 0 1 0 0 3 1.5 1.5 0 0 0 0-3M21 44.5a3.5 3.5 0 1 1 7 0 3.5 3.5 0 0 1-7 0m3.5-1.5a1.5 1.5 0 1 0 0 3 1.5 1.5 0 0 0 0-3m20-23a3.5 3.5 0 1 0 0 7 3.5 3.5 0 0 0 0-7M43 23.5a1.5 1.5 0 1 1 3 0 1.5 1.5 0 0 1-3 0m-23.23-3.14a1 1 0 0 1-.13 1.4l-2.08 1.74 2.08 1.73a1 1 0 1 1-1.28 1.54l-2.42-2.02a1.63 1.63 0 0 1 0-2.5l2.42-2.02a1 1 0 0 1 1.4.13m7.6 1.41a1 1 0 1 1 1.28-1.54l2.42 2.02c.78.65.78 1.85 0 2.5l-2.42 2.02a1 1 0 1 1-1.28-1.54l2.08-1.73zM24.12 18a1 1 0 0 1 .87 1.12l-1 8a1 1 0 1 1-1.98-.24l1-8a1 1 0 0 1 1.11-.87M12.25 13C11.01 13 10 14 10 15.25v15.5c0 1.24 1 2.25 2.25 2.25h17.33q.09 0 .15.05l4.07 3.05a2 2 0 0 0 3.2-1.6V15.25c0-1.24-1-2.25-2.25-2.25zM12 15.25q.02-.23.25-.25h22.5q.23.02.25.25V34.5l-4.07-3.05q-.6-.45-1.35-.45H12.25a.25.25 0 0 1-.25-.25zm7.24-10.68a1 1 0 1 0-.48-1.94A22 22 0 0 0 2.91 17.7a1 1 0 1 0 1.92.58 20 20 0 0 1 14.4-13.72m11.06-1.65a1 1 0 0 0-.58 1.92c6.45 1.92 11.54 7 13.46 13.46a1 1 0 1 0 1.92-.58 22 22 0 0 0-14.8-14.8M4.57 28.76a1 1 0 0 0-1.94.48 22 22 0 0 0 16.13 16.13 1 1 0 1 0 .48-1.94A20 20 0 0 1 4.57 28.76m40.8.48a1 1 0 1 0-1.94-.48 20 20 0 0 1-13.72 14.41 1 1 0 0 0 .58 1.92 22 22 0 0 0 15.08-15.85"/></svg>
                <h5 class="pt4 fw-bold">Collectives™ on Stack Overflow</h5>
                <p class="my16 fs-caption fc-black-500">Find centralized, trusted content and collaborate around the technologies you use most.</p>
                <a href="/collectives"
            class="js-gps-track s-btn s-btn__filled s-btn__xs"
            data-gps-track="top_nav.click({is_current:false, location:2, destination:18})">
                    Learn more about Collectives
                </a>
            </div>
        </div>

        <div class="s-popover ws2"
        id="popover-teams-create-cta"
        role="menu"
        aria-hidden="true">
            <div class="s-popover--arrow"></div>

            <div class="ps-relative overflow-hidden">
                <p class="mb2"><strong>Teams</strong></p>
                <p class="mb12 fs-caption fc-black-400">Q&amp;A for work</p>
                <p class="mb12 fs-caption fc-black-500">Connect and share knowledge within a single location that is structured and easy to search.</p>
                <a href="https://stackoverflow.co/teams/"
            class="js-gps-track s-btn s-btn__filled s-btn__xs"
            data-gps-track="teams.create.left-sidenav.click({ Action: CtaClick })"
            data-ga="[&quot;teams left navigation - anonymous&quot;,&quot;left nav cta&quot;,&quot;stackoverflow.com/teams&quot;,null,null]">
                    Learn more about Teams
                </a>
            </div>

            <div class="ps-absolute t8 r8">
                <svg aria-hidden="true" class="fc-orange-400 svg-spot spotPeople" width="48" height="48"  viewBox="0 0 48 48"><path  d="M13.5 28a4.5 4.5 0 1 0 0-9 4.5 4.5 0 0 0 0 9M7 30a1 1 0 0 1 1-1h11a1 1 0 0 1 1 1v5h11v-5a1 1 0 0 1 1-1h12a1 1 0 0 1 1 1v10a2 2 0 0 1-2 2H33v5a1 1 0 0 1-1 1H20a1 1 0 0 1-1-1v-5H8a1 1 0 0 1-1-1zm25-6.5a4.5 4.5 0 1 0 9 0 4.5 4.5 0 0 0-9 0M24.5 34a4.5 4.5 0 1 0 0-9 4.5 4.5 0 0 0 0 9" opacity=".2"/><path  d="M16.4 26.08A6 6 0 1 0 7.53 26C5.64 26.06 4 27.52 4 29.45V40a1 1 0 0 0 1 1h9a1 1 0 1 0 0-2h-4v-7a1 1 0 1 0-2 0v7H6v-9.55c0-.73.67-1.45 1.64-1.45H16a1 1 0 0 0 .4-1.92M12 18a4 4 0 1 1 0 8 4 4 0 0 1 0-8m16.47 14a6 6 0 1 0-8.94 0A3.6 3.6 0 0 0 16 35.5V46a1 1 0 0 0 1 1h14a1 1 0 0 0 1-1V35.5c0-1.94-1.64-3.42-3.53-3.5M20 28a4 4 0 1 1 8 0 4 4 0 0 1-8 0m-.3 6h8.6c1 0 1.7.75 1.7 1.5V45h-2v-7a1 1 0 1 0-2 0v7h-4v-7a1 1 0 1 0-2 0v7h-2v-9.5c0-.75.7-1.5 1.7-1.5M42 22c0 1.54-.58 2.94-1.53 4A3.5 3.5 0 0 1 44 29.45V40a1 1 0 0 1-1 1h-9a1 1 0 1 1 0-2h4v-7a1 1 0 1 1 2 0v7h2v-9.55A1.5 1.5 0 0 0 40.48 28H32a1 1 0 0 1-.4-1.92A6 6 0 1 1 42 22m-2 0a4 4 0 1 0-8 0 4 4 0 0 0 8 0"/><g  opacity=".35"><path d="M17 10a1 1 0 011-1h12a1 1 0 110 2H18a1 1 0 01-1-1m1-5a1 1 0 100 2h12a1 1 0 100-2zM14 1a1 1 0 00-1 1v12a1 1 0 001 1h5.09l4.2 4.2a1 1 0 001.46-.04l3.7-4.16H34a1 1 0 001-1V2a1 1 0 00-1-1zm1 12V3h18v10h-5a1 1 0 00-.75.34l-3.3 3.7-3.74-3.75a1 1 0 00-.71-.29z"/></g></svg>
            </div>
        </div>

        <div class="s-popover ws2"
             id="popover-labs-left-nav"
             role="menu"
             aria-hidden="true">
            <div class="s-popover--arrow"></div>
            <svg aria-hidden="true" class="fc-black-600 mb8 svg-icon iconLabsAltSm" width="42" height="18"  viewBox="0 0 42 18"><path fill="var(--black-600)" d="M11.5 13.62c0 .21-.17.38-.37.38H5.36a.37.37 0 0 1-.37-.38V4.38c0-.21.17-.38.37-.38h1.26c.2 0 .37.17.37.38v7.6h4.14c.2 0 .37.18.37.38zm9.43.22a.4.4 0 0 1-.3.16h-1.5q-.25-.01-.36-.25l-.55-1.7h-3.1l-.56 1.7a.4.4 0 0 1-.35.25h-1.5a.38.38 0 0 1-.35-.5l3.39-9.25c.05-.15.2-.25.35-.25h1.13q.26.01.36.25l3.39 9.24q.06.19-.05.35m-4.16-7.39-1.21 3.53h2.26zm13.34 5.71a.37.37 0 0 0 0 .53A4.5 4.5 0 0 0 33.59 14c1.02 0 1.92-.27 2.58-.79a2.8 2.8 0 0 0 1.07-2.25c0-.86-.27-1.62-.87-2.15-.46-.4-1-.63-1.89-.76l-1.04-.16a2 2 0 0 1-.83-.33q-.22-.19-.22-.57 0-.46.3-.73c.2-.18.53-.32 1-.32.7 0 1.25.15 1.72.6.14.14.37.14.52 0l.88-.87a.37.37 0 0 0-.01-.53A4.2 4.2 0 0 0 33.72 4c-1.01 0-1.87.3-2.48.84a3 3 0 0 0-.93 2.2q-.02 1.24.78 2.01.72.66 1.93.83l1.07.15c.5.07.65.15.8.29q.23.2.24.67-.01.5-.35.73-.34.29-1.16.3c-.87 0-1.49-.19-2.07-.76a.37.37 0 0 0-.52 0zM22.37 14a.37.37 0 0 1-.37-.38V4.38c0-.21.17-.38.37-.38h3.54q1.4 0 2.26.78c.56.52.86 1.26.86 2.13 0 .84-.37 1.52-.87 1.95A2.6 2.6 0 0 1 29.17 11q0 1.42-.9 2.23c-.56.51-1.34.76-2.22.76zm3.54-1.98c.96 0 .96-1 .96-1s0-1.02-.96-1.02H24v2.02zm-.11-4.06c1.07 0 1.07-1.02 1.07-1.02s0-1.01-1.07-1.01H24v2.03zM0 4v10a4 4 0 0 0 4 4h34a4 4 0 0 0 4-4V4a4 4 0 0 0-4-4H4a4 4 0 0 0-4 4m4-2h34a2 2 0 0 1 2 2v10a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V4c0-1.1.9-2 2-2"/></svg>
            <p class="fs-caption">Get early access and see previews of new features.</p>
            <a class="s-btn s-btn__filled s-btn__xs s-btn__icon fs-fine" href="https://stackoverflow.co/labs/"><svg aria-hidden="true" class="svg-icon iconShareSm" width="14" height="14"  viewBox="0 0 14 14"><path  d="M5 1H3a2 2 0 0 0-2 2v8c0 1.1.9 2 2 2h8a2 2 0 0 0 2-2V9h-2v2H3V3h2zm2 0h6v6h-2V4.5L6.5 9 5 7.5 9.5 3H7z"/></svg> Learn more about Labs</a>
        </div>



</div>



        <div id="content" class="snippet-hidden">

            

<div itemprop="mainEntity" itemscope itemtype="https://schema.org/Question">
    <link itemprop="image" href="https://cdn.sstatic.net/Sites/stackoverflow/Img/apple-touch-icon.png?v=c78bd457575a">

    <div class="inner-content clearfix">
        

            <div id="question-header" class="d-flex sm:fd-column">
                        <h1 itemprop="name" class="fs-headline1 ow-break-word mb8 flex--item fl1"><a href="/questions/35302978/how-to-get-current-value-of-androids-proximity-sensor" class="question-hyperlink">How to get current value of Android&#39;s proximity sensor?</a></h1>

                <div class="ml12 aside-cta flex--item sm:ml0 sm:mb12 sm:order-first d-flex jc-end">

                        <div class="ml12 aside-cta flex--item print:d-none">
                                <a href="/questions/ask" class="ws-nowrap s-btn s-btn__filled">
        Ask Question
    </a>

                        </div>
                </div>
            </div>
            <div class="d-flex fw-wrap pb8 mb16 bb bc-black-200">
                    <div class="flex--item ws-nowrap mr16 mb8" title="2016-02-09 21:56:37Z">
                        <span class="fc-black-400 mr2">Asked</span>
                        <time itemprop="dateCreated" datetime="2016-02-09T21:56:37">8 years, 10 months ago</time>
                    </div>
                    <div class="flex--item ws-nowrap mr16 mb8">
                        <span class="fc-black-400 mr2">Modified</span>
                        <a href="?lastactivity" class="s-link s-link__inherit" title="2017-05-11 06:05:42Z">7 years, 7 months ago</a>
                    </div>
                    <div class="flex--item ws-nowrap mb8 mr16" title="Viewed 7,728 times">
                        <span class="fc-black-400 mr2">Viewed</span>
                        8k times
                    </div>
                        <div class="flex--item mb8 fc-black-400">
                            <svg aria-hidden="true" class="fc-orange-400 svg-icon iconStarVerified" width="18" height="18"  viewBox="0 0 18 18"><path  d="M9.86.89a1.14 1.14 0 0 0-1.72 0l-.5.58c-.3.35-.79.48-1.23.33l-.72-.25a1.14 1.14 0 0 0-1.49.85l-.14.76c-.1.45-.45.8-.9.9l-.76.14c-.67.14-1.08.83-.85 1.49l.25.72c.15.44.02.92-.33 1.23l-.58.5a1.14 1.14 0 0 0 0 1.72l.58.5c.35.3.48.79.33 1.23l-.25.72c-.23.66.18 1.35.85 1.49l.76.14c.45.1.8.45.9.9l.14.76c.14.67.83 1.08 1.49.85l.72-.25c.44-.15.92-.02 1.23.33l.5.58c.46.52 1.26.52 1.72 0l.5-.58c.3-.35.79-.48 1.23-.33l.72.25c.66.23 1.35-.18 1.49-.85l.14-.76c.1-.45.45-.8.9-.9l.76-.14c.67-.14 1.08-.83.85-1.49l-.25-.72c-.15-.44-.02-.92.33-1.23l.58-.5c.52-.46.52-1.26 0-1.72l-.58-.5c-.35-.3-.48-.79-.33-1.23l.25-.72a1.14 1.14 0 0 0-.85-1.49l-.76-.14c-.45-.1-.8-.45-.9-.9l-.14-.76a1.14 1.14 0 0 0-1.49-.85l-.72.25c-.44.15-.92.02-1.23-.33zm-.49 2.67L10.6 6.6q.1.23.34.25l3.26.22c.36.03.5.48.23.71l-2.5 2.1a.4.4 0 0 0-.14.4l.8 3.16a.4.4 0 0 1-.6.44L9.2 12.13a.4.4 0 0 0-.42 0l-2.77 1.74a.4.4 0 0 1-.6-.44l.8-3.16a.4.4 0 0 0-.13-.4l-2.5-2.1a.4.4 0 0 1 .22-.7l3.26-.23a.4.4 0 0 0 .34-.25l1.22-3.03a.4.4 0 0 1 .74 0"/></svg> Part of <a href ="/collectives/mobile-dev" class="js-gps-track " data-gps-track="subcommunity_link.click({ subcommunity_user_type: 0, subcommunity_slug: mobile-dev, link_source: post_header })">Mobile Development</a> Collective
                        </div>
            </div>



            <div id="mainbar" role="main" aria-label="question and answers">
                
<div class="question js-question" data-questionid="35302978" data-position-on-page="0" data-score="7"  id="question">
    <style>
    </style>
<div class="js-zone-container zone-container-main">
    <div id="dfp-tlb" class="everyonelovesstackoverflow everyoneloves__top-leaderboard everyoneloves__leaderboard"></div>
		<div class="js-report-ad-button-container " style="width: 728px"></div>
</div>

    <div class="post-layout ">
        <div class="votecell post-layout--left">
            

<div class="js-voting-container d-flex jc-center fd-column ai-center gs4 fc-black-300" data-post-id="35302978" data-referrer="None">
        <button class="js-vote-up-btn flex--item s-btn s-btn__muted s-btn__outlined bar-pill bc-black-225 f:bc-theme-secondary-400 f:bg-theme-secondary-400 f:fc-black-050 h:bg-theme-primary-200"
                data-controller="s-tooltip"
                data-s-tooltip-placement="right"
                title="This question shows research effort; it is useful and clear"
                aria-pressed="false"
                aria-label="Up vote"
                data-selected-classes="fc-theme-primary bc-theme-primary bg-theme-primary-100"
                data-unselected-classes="bc-black-225 f:bc-theme-secondary-400 f:bg-theme-secondary-400 f:fc-black-050 h:bg-theme-primary-200">
            <svg aria-hidden="true" class="svg-icon iconArrowUp" width="18" height="18"  viewBox="0 0 18 18"><path  d="M1 12h16L9 4z"/></svg>
        </button>
        <input type="hidden" id="voteUpHash" value="70:3:31e,16:67cba4c4bcc76948,10:1734583726,16:ea0fd38e63765d5a,8:35302978,08e0e981f3abd2b35ea49c64bb9ebc3c0ff28d8f96c173d30144d41c9c6b06af" />
        <div class="js-vote-count flex--item d-flex fd-column ai-center fc-theme-body-font fw-bold fs-subheading py4"
             itemprop="upvoteCount"
             data-value="7">
            7
        </div>
        <button
                class="js-vote-down-btn js-vote-down-question flex--item mb8 s-btn s-btn__muted s-btn__outlined bar-pill bc-black-225 f:bc-theme-secondary-400 f:bg-theme-secondary-400 f:fc-black-050 h:bg-theme-primary-200"
                title="This question does not show any research effort; it is unclear or not useful"
                aria-pressed="false"
                aria-label="Down vote"
                data-selected-classes="fc-theme-primary bc-theme-primary bg-theme-primary-100"
                data-unselected-classes="bc-black-225 f:bc-theme-secondary-400 f:bg-theme-secondary-400 f:fc-black-050 h:bg-theme-primary-200">
            <svg aria-hidden="true" class="svg-icon iconArrowDown" width="18" height="18"  viewBox="0 0 18 18"><path  d="M1 6h16l-8 8z"/></svg>
        </button>
        <input type="hidden" id="voteDownHash" value="70:3:31e,16:9aa5c7ae33a960d9,10:1734583726,16:328cbbb639914577,8:35302978,eb20b20b2c4e5ca632a61652210c5bb4f6bdeb74cd5094dccdbaaf9d7e99fd81" />


        
<button class="js-saves-btn s-btn s-btn__unset c-pointer py4"
        type="button"
        id="saves-btn-35302978"
        data-controller="s-tooltip"
        data-s-tooltip-placement="right"
        data-s-popover-placement=""
        title="Save this question."
        data-is-saved="false"
        aria-label="Save"
        data-post-id="35302978"
        data-post-type-id="1"
        data-user-privilege-for-post-click="0"
        aria-controls=""
        data-s-popover-auto-show="false"
>
    <svg aria-hidden="true" class="fc-theme-primary-400 js-saves-btn-selected d-none svg-icon iconBookmark" width="18" height="18"  viewBox="0 0 18 18"><path  d="M3 17V3c0-1.1.9-2 2-2h8a2 2 0 0 1 2 2v14l-6-4z"/></svg>
    <svg aria-hidden="true" class="js-saves-btn-unselected svg-icon iconBookmarkAlt" width="18" height="18"  viewBox="0 0 18 18"><path  d="m9 10.6 4 2.66V3H5v10.26zM3 17V3c0-1.1.9-2 2-2h8a2 2 0 0 1 2 2v14l-6-4z"/></svg>
</button>








    
    <a class="js-post-issue flex--item s-btn s-btn__unset c-pointer py6 mx-auto" href="/posts/35302978/timeline" data-shortcut="T" data-ks-title="timeline" data-controller="s-tooltip" data-s-tooltip-placement="right" title="Show activity on this post." aria-label="Timeline"><svg aria-hidden="true" class="mln2 mr0 svg-icon iconHistory" width="19" height="18"  viewBox="0 0 19 18"><path  d="M3 9a8 8 0 1 1 3.73 6.77L8.2 14.3A6 6 0 1 0 5 9l3.01-.01-4 4-4-4zm7-4h1.01L11 9.36l3.22 2.1-.6.93L10 10z"/></svg></a>

</div>

        </div>

        

<div class="postcell post-layout--right">
    
    <div class="s-prose js-post-body" itemprop="text">
                
<p>Is it possible to get the current value of the Proximity Sensor in Android?  </p>

<p>I know that I can use SensorManager and Sensor and register a state changed listener, but I have no need to be notified of every state change, so it would be highly inefficient since this code is being run in a service.  Also, my code won't know the value until a state change has occurred (what if the value hasn't changed...how do I know what it is?  Instead, rather than registering a listener, I just want to say:</p>

<pre><code>proximitySensor.getCurrentDistance();
</code></pre>

<p>Is this possible?</p>

<p>Thanks</p>
    </div>

        <div class="mt24 mb12">
            <div class="post-taglist d-flex gs4 gsy fd-column">
                <div class="d-flex ps-relative fw-wrap">
                    <a class="themed subcommunity-topic-avatar subcommunity-topic-mobile-dev s-avatar s-avatar__24 mr2 js-community-tag my2 mr6 va-top" style="" data-controller="s-tooltip" title="Mobile Development Collective" href="/collectives/mobile-dev"></a>
                    <ul class='ml0 list-ls-none js-post-tag-list-wrapper d-inline'><li class='d-inline mr4 js-post-tag-list-item'><a href="/questions/tagged/android" class="s-tag post-tag" title="show questions tagged &#39;android&#39;" aria-label="show questions tagged &#39;android&#39;" rel="tag" aria-labelledby="tag-android-tooltip-container" data-tag-menu-origin="Unknown">android</a></li><li class='d-inline mr4 js-post-tag-list-item'><a href="/questions/tagged/android-sensors" class="s-tag post-tag" title="show questions tagged &#39;android-sensors&#39;" aria-label="show questions tagged &#39;android-sensors&#39;" rel="tag" aria-labelledby="tag-android-sensors-tooltip-container" data-tag-menu-origin="Unknown">android-sensors</a></li><li class='d-inline mr4 js-post-tag-list-item'><a href="/questions/tagged/sensormanager" class="s-tag post-tag" title="show questions tagged &#39;sensormanager&#39;" aria-label="show questions tagged &#39;sensormanager&#39;" rel="tag" aria-labelledby="tag-sensormanager-tooltip-container" data-tag-menu-origin="Unknown">sensormanager</a></li><li class='d-inline mr4 js-post-tag-list-item'><a href="/questions/tagged/android-developer-api" class="s-tag post-tag" title="show questions tagged &#39;android-developer-api&#39;" aria-label="show questions tagged &#39;android-developer-api&#39;" rel="tag" aria-labelledby="tag-android-developer-api-tooltip-container" data-tag-menu-origin="Unknown">android-developer-api</a></li><li class='d-inline mr4 js-post-tag-list-item'><a href="/questions/tagged/proximitysensor" class="s-tag post-tag" title="show questions tagged &#39;proximitysensor&#39;" aria-label="show questions tagged &#39;proximitysensor&#39;" rel="tag" aria-labelledby="tag-proximitysensor-tooltip-container" data-tag-menu-origin="Unknown">proximitysensor</a></li></ul>
                </div>
            </div>
        </div>

    <div class="mb0 ">
        <div class="mt16 d-flex gs8 gsy fw-wrap jc-end ai-start pt4 mb16">
            <div class="flex--item mr16 fl1 w96">
                


<div class="js-post-menu pt2" data-post-id="35302978" data-post-type-id="1">

    <div class="d-flex gs8 s-anchors s-anchors__muted fw-wrap">

        <div class="flex--item">
            <a href="/q/35302978"
               rel="nofollow"
               itemprop="url"
               class="js-share-link js-gps-track"
               title="Short permalink to this question"
               data-gps-track="post.click({ item: 2, priv: 0, post_type: 1 })"
               data-controller="se-share-sheet"
               data-se-share-sheet-title="Share a link to this question"
               data-se-share-sheet-subtitle=""
               data-se-share-sheet-post-type="question"
               data-se-share-sheet-social="facebook twitter devto"
               data-se-share-sheet-location="1"
               data-se-share-sheet-license-url="https%3a%2f%2fcreativecommons.org%2flicenses%2fby-sa%2f3.0%2f"
               data-se-share-sheet-license-name="CC BY-SA 3.0"
               data-s-popover-placement="bottom-start">Share</a>
        </div>


                    <div class="flex--item">
                        <a href="/posts/35302978/edit" class="js-suggest-edit-post js-gps-track" data-gps-track="post.click({ item: 6, priv: 0, post_type: 1 })" title="">Improve this question</a>
                    </div>

                <div class="flex--item">
                    <button type="button"
                            id="btnFollowPost-35302978" class="s-btn s-btn__link js-follow-post js-follow-question js-gps-track"
                            data-gps-track="post.click({ item: 14, priv: 0, post_type: 1 })"
                            data-controller="s-tooltip " data-s-tooltip-placement="bottom"
                            data-s-popover-placement="bottom" aria-controls=""
                            title="Follow this question to receive notifications">
                        Follow
                        <input type="hidden" id="voteFollowHash" value="70:3:31e,16:0f31ffe22dde3b7a,10:1734583726,16:bb7fd10eaae29ba1,8:35302978,f160a332c06fa85b55c1d0d7aa465ffe11d7996d9aec7c7627e3135d7016aeb9" />
                    </button>
                </div>






    </div>
    <div class="js-menu-popup-container"></div>
</div>
            </div>

                <div class="post-signature flex--item">
<div class="user-info ">
    <div class="d-flex ">
        <div class="user-action-time fl-grow1">
            <a href="/posts/35302978/revisions" title="show all edits to this post"
                         class="js-gps-track"
                         data-gps-track="post.click({ item: 4, priv: 0, post_type: 1 })">edited <span title='2016-02-10 01:43:41Z' class='relativetime'>Feb 10, 2016 at 1:43</span></a>
        </div>
        
    </div>
    <div class="user-gravatar32">
        
    </div>
    <div class="user-details" itemprop="author" itemscope itemtype="http://schema.org/Person">
        <span class="d-none" itemprop="name">Nullqwerty</span>
        <div class="-flair">
            
        </div>
    </div>
</div>
                </div>
            <div class="post-signature owner flex--item">
                <div class="user-info ">
    <div class="d-flex ">
        <div class="user-action-time fl-grow1">
            asked <span title='2016-02-09 21:56:37Z' class='relativetime'>Feb 9, 2016 at 21:56</span>
        </div>
        
    </div>
    <div class="user-gravatar32">
        <a href="/users/557596/nullqwerty"><div class="gravatar-wrapper-32"><img src="https://www.gravatar.com/avatar/aac9a511d0a7fd4b9b8d93ab85697a2e?s=64&amp;d=identicon&amp;r=PG" alt="Nullqwerty&#39;s user avatar" width="32" height="32" class="bar-sm"></div></a>
    </div>
    <div class="user-details" itemprop="author" itemscope itemtype="http://schema.org/Person">
        <a href="/users/557596/nullqwerty">Nullqwerty</a><span class="d-none" itemprop="name">Nullqwerty</span>
        <div class="-flair">
            <span class="reputation-score" title="reputation score " dir="ltr">1,168</span><span title="1 gold badge" aria-hidden="true"><span class="badge1"></span><span class="badgecount">1</span></span><span class="v-visible-sr">1 gold badge</span><span title="21 silver badges" aria-hidden="true"><span class="badge2"></span><span class="badgecount">21</span></span><span class="v-visible-sr">21 silver badges</span><span title="38 bronze badges" aria-hidden="true"><span class="badge3"></span><span class="badgecount">38</span></span><span class="v-visible-sr">38 bronze badges</span>
        </div>
    </div>
</div>


            </div>
        </div>
    </div>
    
</div>




            <span class="d-none" itemprop="commentCount"></span> 
    <div class="post-layout--right js-post-comments-component">
        <div id="comments-35302978" class="comments js-comments-container bt bc-black-200 mt12  dno" data-post-id="35302978" data-min-length="15">
            <ul class="comments-list js-comments-list"
                    data-remaining-comments-count="0"
                    data-canpost="false"
                    data-cansee="true"
                    data-comments-unavailable="false"
                    data-addlink-disabled="true">

            </ul>
	    </div>

        <div id="comments-link-35302978" data-rep=50 data-anon=true>
                    <a class="js-add-link comments-link disabled-link" title="Use comments to ask for more information or suggest improvements. Avoid answering questions in comments."  href="#" role="button">Add a comment</a>
                <span class="js-link-separator dno">&nbsp;|&nbsp;</span>
            <a class="js-show-link comments-link dno" title="Expand to show all comments on this post" href=# onclick="" role="button"></a>
        </div>         
    </div>
    </div>

</div>


<div class="js-zone-container zone-container-responsive">
    <div id="dfp-isb" class="everyonelovesstackoverflow everyoneloves__inline-sidebar mx-auto"></div>
		<div class="js-report-ad-button-container mx-auto" style="width: 300px"></div>
</div>

                
                <div id="answers">
                    <a name="tab-top"></a>
                    <div id="answers-header">
                        <div class="answers-subheader d-flex ai-center mb8">
                            <div class="flex--item fl1">
                                <h2 class="mb0" data-answercount="2">
                                        2 Answers
                                    <span style="display:none;" itemprop="answerCount">2</span>
                                </h2>
                            </div>
                            <div class="flex--item">
                                

<div class="d-flex g4 gsx ai-center sm:fd-column sm:ai-start">
    <div class="d-flex fd-column ai-end sm:ai-start">
        <label class="flex--item fs-caption" for="answer-sort-dropdown-select-menu">
            Sorted by:
        </label>
        <a 
            class="js-sort-preference-change s-link flex--item fs-fine d-none"
            data-value="ScoreDesc"
            href="/questions/35302978/how-to-get-current-value-of-androids-proximity-sensor?answertab=scoredesc#tab-top"
        >
            Reset to default
        </a>
    </div>
    <div class="flex--item s-select">
        <select id="answer-sort-dropdown-select-menu">
                    <option
                        value=scoredesc
                        selected=selected
                    >
                        Highest score (default)
                    </option>
                    <option
                        value=trending
                    >
                        Trending (recent votes count more)
                    </option>
                    <option
                        value=modifieddesc
                    >
                        Date modified (newest first)
                    </option>
                    <option
                        value=createdasc
                    >
                        Date created (oldest first)
                    </option>
        </select>
    </div>
</div>


                            </div>
                        </div>
                            
                    </div>


                                    
<a name="35303482"></a>
<div id="answer-35303482" class="answer js-answer" data-answerid="35303482" data-parentid="35302978" data-score="4" data-position-on-page="1" data-highest-scored="1" data-question-has-accepted-highest-score="0"  itemprop="acceptedAnswer" itemscope itemtype="https://schema.org/Answer">
        <div class="post-layout">
            <div class="votecell post-layout--left">
                

<div class="js-voting-container d-flex jc-center fd-column ai-center gs4 fc-black-300" data-post-id="35303482" data-referrer="None">
        <button class="js-vote-up-btn flex--item s-btn s-btn__muted s-btn__outlined bar-pill bc-black-225 f:bc-theme-secondary-400 f:bg-theme-secondary-400 f:fc-black-050 h:bg-theme-primary-200"
                data-controller="s-tooltip"
                data-s-tooltip-placement="right"
                title="This answer is useful"
                aria-pressed="false"
                aria-label="Up vote"
                data-selected-classes="fc-theme-primary bc-theme-primary bg-theme-primary-100"
                data-unselected-classes="bc-black-225 f:bc-theme-secondary-400 f:bg-theme-secondary-400 f:fc-black-050 h:bg-theme-primary-200">
            <svg aria-hidden="true" class="svg-icon iconArrowUp" width="18" height="18"  viewBox="0 0 18 18"><path  d="M1 12h16L9 4z"/></svg>
        </button>
        <input type="hidden" id="voteUpHash" value="70:3:31e,16:f57bfdadd5364a45,10:1734583726,16:b7461774d276dae2,8:35303482,c5393bd8bce993b325fe8d08448d322a54cf2da1e5833b38e85cb4f46440869e" />
        <div class="js-vote-count flex--item d-flex fd-column ai-center fc-theme-body-font fw-bold fs-subheading py4"
             itemprop="upvoteCount"
             data-value="4">
            4
        </div>
        <button
                class="js-vote-down-btn flex--item mb8 s-btn s-btn__muted s-btn__outlined bar-pill bc-black-225 f:bc-theme-secondary-400 f:bg-theme-secondary-400 f:fc-black-050 h:bg-theme-primary-200"
                title="This answer is not useful"
                aria-pressed="false"
                aria-label="Down vote"
                data-selected-classes="fc-theme-primary bc-theme-primary bg-theme-primary-100"
                data-unselected-classes="bc-black-225 f:bc-theme-secondary-400 f:bg-theme-secondary-400 f:fc-black-050 h:bg-theme-primary-200">
            <svg aria-hidden="true" class="svg-icon iconArrowDown" width="18" height="18"  viewBox="0 0 18 18"><path  d="M1 6h16l-8 8z"/></svg>
        </button>
        <input type="hidden" id="voteDownHash" value="70:3:31e,16:acdd4c44bc5ba6cd,10:1734583726,16:e03cd7d2121e6883,8:35303482,734b584174ae1939b0f6fa327bff62fc310032d7cb50b1de6c3735027ce16d84" />


        
<button class="js-saves-btn s-btn s-btn__unset c-pointer py4"
        type="button"
        id="saves-btn-35303482"
        data-controller="s-tooltip"
        data-s-tooltip-placement="right"
        data-s-popover-placement=""
        title="Save this answer."
        data-is-saved="false"
        aria-label="Save"
        data-post-id="35303482"
        data-post-type-id="2"
        data-user-privilege-for-post-click="0"
        aria-controls=""
        data-s-popover-auto-show="false"
>
    <svg aria-hidden="true" class="fc-theme-primary-400 js-saves-btn-selected d-none svg-icon iconBookmark" width="18" height="18"  viewBox="0 0 18 18"><path  d="M3 17V3c0-1.1.9-2 2-2h8a2 2 0 0 1 2 2v14l-6-4z"/></svg>
    <svg aria-hidden="true" class="js-saves-btn-unselected svg-icon iconBookmarkAlt" width="18" height="18"  viewBox="0 0 18 18"><path  d="m9 10.6 4 2.66V3H5v10.26zM3 17V3c0-1.1.9-2 2-2h8a2 2 0 0 1 2 2v14l-6-4z"/></svg>
</button>







            <div class="js-accepted-answer-indicator flex--item fc-green-400 py6 mtn8 d-none" data-s-tooltip-placement="right" title="Loading when this answer was accepted&#x2026;" tabindex="0" role="note" aria-label="Accepted">
                <div class="ta-center">
                    <svg aria-hidden="true" class="svg-icon iconCheckmarkLg" width="36" height="36"  viewBox="0 0 36 36"><path  d="m6 14 8 8L30 6v8L14 30l-8-8z"/></svg>
                </div>
            </div>

    
    <a class="js-post-issue flex--item s-btn s-btn__unset c-pointer py6 mx-auto" href="/posts/35303482/timeline" data-shortcut="T" data-ks-title="timeline" data-controller="s-tooltip" data-s-tooltip-placement="right" title="Show activity on this post." aria-label="Timeline"><svg aria-hidden="true" class="mln2 mr0 svg-icon iconHistory" width="19" height="18"  viewBox="0 0 19 18"><path  d="M3 9a8 8 0 1 1 3.73 6.77L8.2 14.3A6 6 0 1 0 5 9l3.01-.01-4 4-4-4zm7-4h1.01L11 9.36l3.22 2.1-.6.93L10 10z"/></svg></a>

</div>

            </div>

            

<div class="answercell post-layout--right">
        <div class="js-endorsements" data-for-answer="35303482">
</div>

    
    <div class="s-prose js-post-body" itemprop="text">
<p>After looking through the documentation, it looks like you can get the distance in centimeters by subscribing to the SensorEvent and looking at the data being passed back. </p>

<p>There is a good example of starting to use the Proximity sensor here: <a href="http://androidbite.blogspot.com/2013/05/android-proximity-sensor-example.html" rel="nofollow">Android Proximity Sensor Example</a></p>

<p>After reading a bit further into the Android <a href="http://developer.android.com/reference/android/hardware/SensorEvent.html#values" rel="nofollow">docs</a>, it looks like the array <code>values[0]</code> returns a value in centimeters. Note, look at the docs, some sensors only return binary values, meaning that the device is either near or far.</p>
    </div>
    <div class="mt24">
        <div class="d-flex fw-wrap ai-start jc-end gs8 gsy">
            <time itemprop="dateCreated" datetime="2016-02-09T22:31:22"></time>
            <div class="flex--item mr16" style="flex: 1 1 100px;">
                


<div class="js-post-menu pt2" data-post-id="35303482" data-post-type-id="2">

    <div class="d-flex gs8 s-anchors s-anchors__muted fw-wrap">

        <div class="flex--item">
            <a href="/a/35303482"
               rel="nofollow"
               itemprop="url"
               class="js-share-link js-gps-track"
               title="Short permalink to this answer"
               data-gps-track="post.click({ item: 2, priv: 0, post_type: 2 })"
               data-controller="se-share-sheet"
               data-se-share-sheet-title="Share a link to this answer"
               data-se-share-sheet-subtitle=""
               data-se-share-sheet-post-type="answer"
               data-se-share-sheet-social="facebook twitter devto"
               data-se-share-sheet-location="2"
               data-se-share-sheet-license-url="https%3a%2f%2fcreativecommons.org%2flicenses%2fby-sa%2f3.0%2f"
               data-se-share-sheet-license-name="CC BY-SA 3.0"
               data-s-popover-placement="bottom-start">Share</a>
        </div>


                    <div class="flex--item">
                        <a href="/posts/35303482/edit" class="js-suggest-edit-post js-gps-track" data-gps-track="post.click({ item: 6, priv: 0, post_type: 2 })" title="">Improve this answer</a>
                    </div>

                <div class="flex--item">
                    <button type="button"
                            id="btnFollowPost-35303482" class="s-btn s-btn__link js-follow-post js-follow-answer js-gps-track"
                            data-gps-track="post.click({ item: 14, priv: 0, post_type: 2 })"
                            data-controller="s-tooltip " data-s-tooltip-placement="bottom"
                            data-s-popover-placement="bottom" aria-controls=""
                            title="Follow this answer to receive notifications">
                        Follow
                        <input type="hidden" id="voteFollowHash" value="70:3:31e,16:257a743bd3d8259a,10:1734583726,16:b582846b84b464ce,8:35303482,055bf0646455bff7d9227aeac28c8461d4245b0721d656b398c12a840c89c972" />
                    </button>
                </div>






    </div>
    <div class="js-menu-popup-container"></div>
</div>
            </div>


            <div class="post-signature flex--item fl0">
                <div class="user-info ">
    <div class="d-flex ">
        <div class="user-action-time fl-grow1">
            answered <span title='2016-02-09 22:31:22Z' class='relativetime'>Feb 9, 2016 at 22:31</span>
        </div>
        
    </div>
    <div class="user-gravatar32">
        <a href="/users/3924722/user3924722"><div class="gravatar-wrapper-32"><img src="https://www.gravatar.com/avatar/97255a93a922300e85d390ce59559a0f?s=64&amp;d=identicon&amp;r=PG&amp;f=y&amp;so-version=2" alt="user3924722&#39;s user avatar" width="32" height="32" class="bar-sm"></div></a>
    </div>
    <div class="user-details" itemprop="author" itemscope itemtype="http://schema.org/Person">
        <a href="/users/3924722/user3924722">user3924722</a><span class="d-none" itemprop="name">user3924722</span>
        <div class="-flair">
            <span class="reputation-score" title="reputation score " dir="ltr">49</span><span title="2 bronze badges" aria-hidden="true"><span class="badge3"></span><span class="badgecount">2</span></span><span class="v-visible-sr">2 bronze badges</span>
        </div>
    </div>
</div>


            </div>
        </div>
        
    
    </div>
    
</div>




                <span class="d-none" itemprop="commentCount">4</span> 
    <div class="post-layout--right js-post-comments-component">
        <div id="comments-35303482" class="comments js-comments-container bt bc-black-200 mt12 " data-post-id="35303482" data-min-length="15">
            <ul class="comments-list js-comments-list"
                    data-remaining-comments-count="0"
                    data-canpost="false"
                    data-cansee="true"
                    data-comments-unavailable="false"
                    data-addlink-disabled="true">

                        <li id="comment-58321170" class="comment js-comment " data-comment-id="58321170" data-comment-owner-id="557596" data-comment-score="1">
        <div class="js-comment-actions comment-actions">
            <div class="comment-score js-comment-score js-comment-edit-hide">
                    <span title="number of &#x27;useful comment&#x27; votes received"
                            class="cool">1</span>
            </div>
        </div>
        <div class="comment-text  js-comment-text-and-form">
            <div class="comment-body js-comment-edit-hide">
                
                <span class="comment-copy">Yes, but I&#39;m asking how to do it without using those listeners.</span>
                
                <div class="d-inline-flex ai-center">
&ndash;&nbsp;<a href="/users/557596/nullqwerty"
                                title="1,168 reputation"
                                class="comment-user owner">Nullqwerty</a>
                </div>
                <span class="comment-date" dir="ltr">
                    <span class="v-visible-sr">Commented</span>
                    <span title='2016-02-10 01:41:47Z, License: CC BY-SA 3.0' class='relativetime-clean'>Feb 10, 2016 at 1:41</span>
                </span>
            </div>
        </div>
    </li>
    <li id="comment-58321176" class="comment js-comment " data-comment-id="58321176" data-comment-owner-id="557596" data-comment-score="0">
        <div class="js-comment-actions comment-actions">
            <div class="comment-score js-comment-score js-comment-edit-hide">
            </div>
        </div>
        <div class="comment-text  js-comment-text-and-form">
            <div class="comment-body js-comment-edit-hide">
                
                <span class="comment-copy">From my post: &quot;I know that I can use SensorManager and Sensor and register a state changed listener, but I have no need to be notified of every state change, so it would be highly inefficient since this code is being run in a service. Also, my code won&#39;t know the value until a state change has occurred (what if the value hasn&#39;t changed...how do I know what it is?&quot;</span>
                
                <div class="d-inline-flex ai-center">
&ndash;&nbsp;<a href="/users/557596/nullqwerty"
                                title="1,168 reputation"
                                class="comment-user owner">Nullqwerty</a>
                </div>
                <span class="comment-date" dir="ltr">
                    <span class="v-visible-sr">Commented</span>
                    <span title='2016-02-10 01:41:54Z, License: CC BY-SA 3.0' class='relativetime-clean'>Feb 10, 2016 at 1:41</span>
                </span>
            </div>
        </div>
    </li>
    <li id="comment-58357709" class="comment js-comment " data-comment-id="58357709" data-comment-owner-id="3924722" data-comment-score="1">
        <div class="js-comment-actions comment-actions">
            <div class="comment-score js-comment-score js-comment-edit-hide">
                    <span title="number of &#x27;useful comment&#x27; votes received"
                            class="cool">1</span>
            </div>
        </div>
        <div class="comment-text  js-comment-text-and-form">
            <div class="comment-body js-comment-edit-hide">
                
                <span class="comment-copy">I apologize, I was multi-tasking while answering, my fault.   I don&#39;t know that there is really any other way than to listen for the changes.</span>
                
                <div class="d-inline-flex ai-center">
&ndash;&nbsp;<a href="/users/3924722/user3924722"
                                title="49 reputation"
                                class="comment-user">user3924722</a>
                </div>
                <span class="comment-date" dir="ltr">
                    <span class="v-visible-sr">Commented</span>
                    <span title='2016-02-10 19:41:37Z, License: CC BY-SA 3.0' class='relativetime-clean'>Feb 10, 2016 at 19:41</span>
                </span>
            </div>
        </div>
    </li>
    <li id="comment-135348868" class="comment js-comment " data-comment-id="135348868" data-comment-owner-id="8864549" data-comment-score="0">
        <div class="js-comment-actions comment-actions">
            <div class="comment-score js-comment-score js-comment-edit-hide">
            </div>
        </div>
        <div class="comment-text  js-comment-text-and-form">
            <div class="comment-body js-comment-edit-hide">
                
                <span class="comment-copy">There appears to be a behavior difference between real device and an emulator: On real device, as soon as I register the listener, the <code>onSensorChanged</code> callback is called.</span>
                
                <div class="d-inline-flex ai-center">
&ndash;&nbsp;<a href="/users/8864549/martin-pt%c3%a1%c4%8dek"
                                title="297 reputation"
                                class="comment-user">Martin Pt&#xE1;&#x10D;ek</a>
                </div>
                <span class="comment-date" dir="ltr">
                    <span class="v-visible-sr">Commented</span>
                    <span title='2023-07-26 17:53:59Z, License: CC BY-SA 4.0' class='relativetime-clean'>Jul 26, 2023 at 17:53</span>
                </span>
            </div>
        </div>
    </li>

            </ul>
	    </div>

        <div id="comments-link-35303482" data-rep=50 data-anon=true>
                    <a class="js-add-link comments-link disabled-link" title="Use comments to ask for more information or suggest improvements. Avoid comments like &#x201C;&#x2B;1&#x201D; or &#x201C;thanks&#x201D;."  href="#" role="button">Add a comment</a>
                <span class="js-link-separator dno">&nbsp;|&nbsp;</span>
            <a class="js-show-link comments-link dno" title="Expand to show all comments on this post" href=# onclick="" role="button"></a>
        </div>         
    </div>
        </div>
</div>
<div class="js-zone-container zone-container-main">
    <div id="dfp-mlb" class="everyonelovesstackoverflow everyoneloves__mid-leaderboard everyoneloves__leaderboard"></div>
		<div class="js-report-ad-button-container " style="width: 728px"></div>
</div>
                                    
<a name="43907683"></a>
<div id="answer-43907683" class="answer js-answer" data-answerid="43907683" data-parentid="35302978" data-score="2" data-position-on-page="2" data-highest-scored="0" data-question-has-accepted-highest-score="0"  itemprop="suggestedAnswer" itemscope itemtype="https://schema.org/Answer">
        <div class="post-layout">
            <div class="votecell post-layout--left">
                

<div class="js-voting-container d-flex jc-center fd-column ai-center gs4 fc-black-300" data-post-id="43907683" data-referrer="None">
        <button class="js-vote-up-btn flex--item s-btn s-btn__muted s-btn__outlined bar-pill bc-black-225 f:bc-theme-secondary-400 f:bg-theme-secondary-400 f:fc-black-050 h:bg-theme-primary-200"
                data-controller="s-tooltip"
                data-s-tooltip-placement="right"
                title="This answer is useful"
                aria-pressed="false"
                aria-label="Up vote"
                data-selected-classes="fc-theme-primary bc-theme-primary bg-theme-primary-100"
                data-unselected-classes="bc-black-225 f:bc-theme-secondary-400 f:bg-theme-secondary-400 f:fc-black-050 h:bg-theme-primary-200">
            <svg aria-hidden="true" class="svg-icon iconArrowUp" width="18" height="18"  viewBox="0 0 18 18"><path  d="M1 12h16L9 4z"/></svg>
        </button>
        <input type="hidden" id="voteUpHash" value="70:3:31e,16:35b7c66a934d5690,10:1734583726,16:d37563f89b788e5a,8:43907683,3d3513421296da0e7f7d8b58f1220cfb8c42f072b8a812c5065250fa51523345" />
        <div class="js-vote-count flex--item d-flex fd-column ai-center fc-theme-body-font fw-bold fs-subheading py4"
             itemprop="upvoteCount"
             data-value="2">
            2
        </div>
        <button
                class="js-vote-down-btn flex--item mb8 s-btn s-btn__muted s-btn__outlined bar-pill bc-black-225 f:bc-theme-secondary-400 f:bg-theme-secondary-400 f:fc-black-050 h:bg-theme-primary-200"
                title="This answer is not useful"
                aria-pressed="false"
                aria-label="Down vote"
                data-selected-classes="fc-theme-primary bc-theme-primary bg-theme-primary-100"
                data-unselected-classes="bc-black-225 f:bc-theme-secondary-400 f:bg-theme-secondary-400 f:fc-black-050 h:bg-theme-primary-200">
            <svg aria-hidden="true" class="svg-icon iconArrowDown" width="18" height="18"  viewBox="0 0 18 18"><path  d="M1 6h16l-8 8z"/></svg>
        </button>
        <input type="hidden" id="voteDownHash" value="70:3:31e,16:19c6527540d36b38,10:1734583726,16:72da5d61dd334322,8:43907683,4e47718bfdb91b10025690261a9b5cb02bdaa2e7699820137cdf8fb856339ddd" />


        
<button class="js-saves-btn s-btn s-btn__unset c-pointer py4"
        type="button"
        id="saves-btn-43907683"
        data-controller="s-tooltip"
        data-s-tooltip-placement="right"
        data-s-popover-placement=""
        title="Save this answer."
        data-is-saved="false"
        aria-label="Save"
        data-post-id="43907683"
        data-post-type-id="2"
        data-user-privilege-for-post-click="0"
        aria-controls=""
        data-s-popover-auto-show="false"
>
    <svg aria-hidden="true" class="fc-theme-primary-400 js-saves-btn-selected d-none svg-icon iconBookmark" width="18" height="18"  viewBox="0 0 18 18"><path  d="M3 17V3c0-1.1.9-2 2-2h8a2 2 0 0 1 2 2v14l-6-4z"/></svg>
    <svg aria-hidden="true" class="js-saves-btn-unselected svg-icon iconBookmarkAlt" width="18" height="18"  viewBox="0 0 18 18"><path  d="m9 10.6 4 2.66V3H5v10.26zM3 17V3c0-1.1.9-2 2-2h8a2 2 0 0 1 2 2v14l-6-4z"/></svg>
</button>







            <div class="js-accepted-answer-indicator flex--item fc-green-400 py6 mtn8 d-none" data-s-tooltip-placement="right" title="Loading when this answer was accepted&#x2026;" tabindex="0" role="note" aria-label="Accepted">
                <div class="ta-center">
                    <svg aria-hidden="true" class="svg-icon iconCheckmarkLg" width="36" height="36"  viewBox="0 0 36 36"><path  d="m6 14 8 8L30 6v8L14 30l-8-8z"/></svg>
                </div>
            </div>

    
    <a class="js-post-issue flex--item s-btn s-btn__unset c-pointer py6 mx-auto" href="/posts/43907683/timeline" data-shortcut="T" data-ks-title="timeline" data-controller="s-tooltip" data-s-tooltip-placement="right" title="Show activity on this post." aria-label="Timeline"><svg aria-hidden="true" class="mln2 mr0 svg-icon iconHistory" width="19" height="18"  viewBox="0 0 19 18"><path  d="M3 9a8 8 0 1 1 3.73 6.77L8.2 14.3A6 6 0 1 0 5 9l3.01-.01-4 4-4-4zm7-4h1.01L11 9.36l3.22 2.1-.6.93L10 10z"/></svg></a>

</div>

            </div>

            

<div class="answercell post-layout--right">
        <div class="js-endorsements" data-for-answer="43907683">
</div>

    
    <div class="s-prose js-post-body" itemprop="text">
<p>To get access the device sensor using SensorManager, you have to  call getSystemService(SENSOR_SERVICE) .  Here is the example:</p>

<pre><code>&lt;RelativeLayout xmlns:android="http://schemas.android.com/apk/res/android"
xmlns:tools="http://schemas.android.com/tools"
android:layout_width="fill_parent"
android:layout_height="fill_parent"
tools:context=".SensorActivity" &gt;

&lt;ImageView
android:id="@+id/imageView1"
android:layout_width="wrap_content"
android:layout_height="wrap_content"
android:src="@drawable/far" /&gt;

&lt;/RelativeLayout&gt;
</code></pre>

<p>Here is the java class:</p>

<pre><code>import android.app.Activity;
import android.hardware.Sensor;
import android.hardware.SensorEvent;
import android.hardware.SensorEventListener;
import android.hardware.SensorManager;
import android.os.Bundle;
import android.widget.ImageView;

public class SensorActivity extends Activity implements SensorEventListener {
 private SensorManager mSensorManager;
 private Sensor mSensor;
 ImageView iv;

 @Override
 protected void onCreate(Bundle savedInstanceState) {
  // TODO Auto-generated method stub
  super.onCreate(savedInstanceState);
  setContentView(R.layout.sensor_screen);
  mSensorManager = (SensorManager) getSystemService(SENSOR_SERVICE);
  mSensor = mSensorManager.getDefaultSensor(Sensor.TYPE_PROXIMITY);
  iv = (ImageView) findViewById(R.id.imageView1);
 }

 protected void onResume() {
  super.onResume();
  mSensorManager.registerListener(this, mSensor,
    SensorManager.SENSOR_DELAY_NORMAL);
 }

 protected void onPause() {
  super.onPause();
  mSensorManager.unregisterListener(this);
 }

 public void onAccuracyChanged(Sensor sensor, int accuracy) {
 }

 public void onSensorChanged(SensorEvent event) {
  if (event.values[0] == 0) {
   iv.setImageResource(R.drawable.near);
  } else {
   iv.setImageResource(R.drawable.far);
  }
 }
}
</code></pre>
    </div>
    <div class="mt24">
        <div class="d-flex fw-wrap ai-start jc-end gs8 gsy">
            <time itemprop="dateCreated" datetime="2017-05-11T06:05:42"></time>
            <div class="flex--item mr16" style="flex: 1 1 100px;">
                


<div class="js-post-menu pt2" data-post-id="43907683" data-post-type-id="2">

    <div class="d-flex gs8 s-anchors s-anchors__muted fw-wrap">

        <div class="flex--item">
            <a href="/a/43907683"
               rel="nofollow"
               itemprop="url"
               class="js-share-link js-gps-track"
               title="Short permalink to this answer"
               data-gps-track="post.click({ item: 2, priv: 0, post_type: 2 })"
               data-controller="se-share-sheet"
               data-se-share-sheet-title="Share a link to this answer"
               data-se-share-sheet-subtitle=""
               data-se-share-sheet-post-type="answer"
               data-se-share-sheet-social="facebook twitter devto"
               data-se-share-sheet-location="2"
               data-se-share-sheet-license-url="https%3a%2f%2fcreativecommons.org%2flicenses%2fby-sa%2f3.0%2f"
               data-se-share-sheet-license-name="CC BY-SA 3.0"
               data-s-popover-placement="bottom-start">Share</a>
        </div>


                    <div class="flex--item">
                        <a href="/posts/43907683/edit" class="js-suggest-edit-post js-gps-track" data-gps-track="post.click({ item: 6, priv: 0, post_type: 2 })" title="">Improve this answer</a>
                    </div>

                <div class="flex--item">
                    <button type="button"
                            id="btnFollowPost-43907683" class="s-btn s-btn__link js-follow-post js-follow-answer js-gps-track"
                            data-gps-track="post.click({ item: 14, priv: 0, post_type: 2 })"
                            data-controller="s-tooltip " data-s-tooltip-placement="bottom"
                            data-s-popover-placement="bottom" aria-controls=""
                            title="Follow this answer to receive notifications">
                        Follow
                        <input type="hidden" id="voteFollowHash" value="70:3:31e,16:2b361fd605b1053b,10:1734583726,16:ff4fa7fc988db467,8:43907683,34f52b0f9a6557289ea26bdad9bda7c71029a18bdac5f38313e5a75c66d09744" />
                    </button>
                </div>






    </div>
    <div class="js-menu-popup-container"></div>
</div>
            </div>


            <div class="post-signature flex--item fl0">
                <div class="user-info user-hover ">
    <div class="d-flex ">
        <div class="user-action-time fl-grow1">
            answered <span title='2017-05-11 06:05:42Z' class='relativetime'>May 11, 2017 at 6:05</span>
        </div>
        
    </div>
    <div class="user-gravatar32">
        <a href="/users/3073945/md-sajedul-karim"><div class="gravatar-wrapper-32"><img src="https://i.sstatic.net/Dig4I.jpg?s=64" alt="Md. Sajedul Karim&#39;s user avatar" width="32" height="32" class="bar-sm"></div></a>
    </div>
    <div class="user-details" itemprop="author" itemscope itemtype="http://schema.org/Person">
        <a href="/users/3073945/md-sajedul-karim">Md. Sajedul Karim</a><span class="d-none" itemprop="name">Md. Sajedul Karim</span>
        <div class="-flair">
            <span class="reputation-score" title="reputation score " dir="ltr">7,025</span><span title="4 gold badges" aria-hidden="true"><span class="badge1"></span><span class="badgecount">4</span></span><span class="v-visible-sr">4 gold badges</span><span title="64 silver badges" aria-hidden="true"><span class="badge2"></span><span class="badgecount">64</span></span><span class="v-visible-sr">64 silver badges</span><span title="89 bronze badges" aria-hidden="true"><span class="badge3"></span><span class="badgecount">89</span></span><span class="v-visible-sr">89 bronze badges</span>
        </div>
    </div>
</div>


            </div>
        </div>
        
    
    </div>
    
</div>




                <span class="d-none" itemprop="commentCount"></span> 
    <div class="post-layout--right js-post-comments-component">
        <div id="comments-43907683" class="comments js-comments-container bt bc-black-200 mt12  dno" data-post-id="43907683" data-min-length="15">
            <ul class="comments-list js-comments-list"
                    data-remaining-comments-count="0"
                    data-canpost="false"
                    data-cansee="true"
                    data-comments-unavailable="false"
                    data-addlink-disabled="true">

            </ul>
	    </div>

        <div id="comments-link-43907683" data-rep=50 data-anon=true>
                    <a class="js-add-link comments-link disabled-link" title="Use comments to ask for more information or suggest improvements. Avoid comments like &#x201C;&#x2B;1&#x201D; or &#x201C;thanks&#x201D;."  href="#" role="button">Add a comment</a>
                <span class="js-link-separator dno">&nbsp;|&nbsp;</span>
            <a class="js-show-link comments-link dno" title="Expand to show all comments on this post" href=# onclick="" role="button"></a>
        </div>         
    </div>
        </div>
</div>

                        <a name='new-answer'></a>
                            <form id="post-form" action="/questions/35302978/answer/submit" method="post" class="js-add-answer-component post-form">
                                <input type="hidden" id="post-id" value="35302978" />
                                <input type="hidden" id="qualityBanWarningShown" name="qualityBanWarningShown" value="false" />
                                <input type="hidden" name="referrer" value="" />
                                <h2 class="space" id="your-answer-header">
                                    Your Answer
                                </h2>
                                    

    <script>
        StackExchange.ifUsing("editor", function () {
            StackExchange.using("externalEditor", function () {
                StackExchange.using("snippets", function () {
                    StackExchange.snippets.init();
                });
            });
        }, "code-snippets");
    </script>


<script>
    StackExchange.ready(function() {
        var channelOptions = {
            tags: "".split(" "),
            id: "1"
        };
        initTagRenderer("".split(" "), "".split(" "), channelOptions);

        StackExchange.using("externalEditor", function() {
            // Have to fire editor after snippets, if snippets enabled
            if (StackExchange.settings.snippets.snippetsEnabled) {
                StackExchange.using("snippets", function() {
                    createEditor();
                });
            }
            else {
                createEditor();
            }
        });

        function createEditor() {   
            StackExchange.prepareEditor({
                useStacksEditor: false,
                heartbeatType: 'answer',
                autoActivateHeartbeat: false,
                convertImagesToLinks: true,
                noModals: true,
                showLowRepImageUploadWarning: true,
                reputationToPostImages: 10,
                bindNavPrevention: true,
                postfix: "",
                imageUploadEnabled: false,
                imageUploader: {
                    brandingHtml: "",
                    contentPolicyHtml: "User contributions licensed under \u003ca href=\"https://stackoverflow.com/help/licensing\"\u003eCC BY-SA\u003c/a\u003e \u003ca href=\"https://stackoverflow.com/legal/acceptable-use-policy\"\u003e(content policy)\u003c/a\u003e",
                    allowUrls: true,
                },
                onDemand: true,
                discardSelector: ".discard-answer",
                enableTables: true,
                isStacksEditorPreviewEnabled: false
                ,enableTables:true,enableSnippets:true
            });
                    }
    });
</script>
<div id="post-editor" class="post-editor js-post-editor d-flex fd-column g4">


        <div class="ps-relative">
            <div class="wmd-container mb8">
                <div id="wmd-button-bar" class="wmd-button-bar btr-sm"></div>
                    <div class="ai-content-policy-notice js-ai-policy-notice fc-black p8 bl br bc-black-300 d-none" aria-hidden="true">
                        <div class="d-flex jc-space-between ac-center gsx gs2">
                            <p class="flex--item as-center"><b>Reminder:</b> Answers generated by artificial intelligence tools are not allowed on Stack Overflow. <a href="/help/gen-ai-policy">Learn more</a></p>
                            <button class="flex--item js-dismiss-ai-banner s-btn s-btn__sm s-btn__icon fc-black"><svg aria-hidden="true" class="svg-icon iconClearSm" width="14" height="14"  viewBox="0 0 14 14"><path  d="M12 3.41 10.59 2 7 5.59 3.41 2 2 3.41 5.59 7 2 10.59 3.41 12 7 8.41 10.59 12 12 10.59 8.41 7z"/></svg></button>
                        </div>
                    </div>
                    <input type="hidden" name="AIPolicyNoticeShown" value="true"/>
                <div class="js-stacks-validation">
                    <div class="ps-relative">
                        <textarea id="wmd-input"
                                  name="post-text"
                                  class="wmd-input s-input bar0 js-post-body-field"
                                  data-editor-type="wmd"
                                  data-post-type-id="2"
                                  cols="92" rows="15"
                                  aria-labelledby="your-answer-header"
                                  tabindex="101"
                                  data-min-length=""></textarea>
                    </div>
                    <div class="s-input-message mt4 d-none js-stacks-validation-message"></div>
                </div>
            </div>
        </div>

    <aside class="d-flex ai-start jc-space-between js-answer-help s-notice s-notice__warning pb0 pr4 pt4 mb8 d-none" role="status" aria-hidden="true">
    <div class="flex--item pt8">
        <p>Thanks for contributing an answer to Stack Overflow!</p><ul><li>Please be sure to <em>answer the question</em>. Provide details and share your research!</li></ul><p>But <em>avoid</em> …</p><ul><li>Asking for help, clarification, or responding to other answers.</li><li>Making statements based on opinion; back them up with references or personal experience.</li></ul><p>To learn more, see our <a href="/help/how-to-answer">tips on writing great answers</a>.</p>
    </div>
    <button class="flex--item js-answer-help-close-btn s-btn s-btn__muted fc-black-600">
        <svg aria-hidden="true" class="svg-icon iconClear" width="18" height="18"  viewBox="0 0 18 18"><path  d="M15 4.41 13.59 3 9 7.59 4.41 3 3 4.41 7.59 9 3 13.59 4.41 15 9 10.41 13.59 15 15 13.59 10.41 9z"/></svg>
    </button>
</aside>



    <div>
        <div id="draft-saved" class="fc-success h24" style="display:none;">Draft saved</div>
        <div id="draft-discarded" class="fc-error h24" style="display:none;">Draft discarded</div>
    </div>


            <div id="wmd-preview" class="s-prose mb16 wmd-preview js-wmd-preview"></div>
            <div></div>

        <div class="edit-block">
            <input id="fkey" name="fkey" type="hidden" value="3263e220c9fc053cefe5230c13d734e7914d13795116a71a9d8e74c9e9fe345a">
            <input id="author" name="author" type="text">
        </div>

</div>


                                <div class="ps-relative">
                                               <div class="form-item dno new-post-login p0 my16">
                <div class="d-flex gs16 md:fd-column new-login-form">
                    <div class="d-flex fd-column w50 md:w-auto gsy gs8 jc-space-between new-login-left">
                        <h3 class="flex--item fs-title">Sign up or <a id="login-link" href="/users/login?ssrc=question_page&returnurl=https%3a%2f%2fstackoverflow.com%2fquestions%2f35302978%2fhow-to-get-current-value-of-androids-proximity-sensor%23new-answer">log in</a></h3>
                        <script>
                            StackExchange.ready(function () {
                                StackExchange.helpers.onClickDraftSave('#login-link');
                            });
                        </script>
                        <div class="flex--item s-btn s-btn__muted s-btn__outlined s-btn__icon google-login" data-ga="[&quot;sign up&quot;,&quot;Sign Up Started - Google&quot;,&quot;New Post&quot;,null,null]">
                            <svg aria-hidden="true" class="native svg-icon iconGoogle" width="18" height="18"  viewBox="0 0 18 18"><path fill="#4285F4" d="M16.51 8H8.98v3h4.3c-.18 1-.74 1.48-1.6 2.04v2.01h2.6a7.8 7.8 0 0 0 2.38-5.88c0-.57-.05-.66-.15-1.18"/><path fill="#34A853" d="M8.98 17c2.16 0 3.97-.72 5.3-1.94l-2.6-2a4.8 4.8 0 0 1-7.18-2.54H1.83v2.07A8 8 0 0 0 8.98 17"/><path fill="#FBBC05" d="M4.5 10.52a4.8 4.8 0 0 1 0-3.04V5.41H1.83a8 8 0 0 0 0 7.18z"/><path fill="#EA4335" d="M8.98 4.18c1.17 0 2.23.4 3.06 1.2l2.3-2.3A8 8 0 0 0 1.83 5.4L4.5 7.49a4.8 4.8 0 0 1 4.48-3.3"/></svg> Sign up using Google
                        </div>
                        <div class="flex--item s-btn s-btn__muted s-btn__outlined s-btn__icon stackexchange-login" data-ga="[&quot;sign up&quot;,&quot;Sign Up Navigation&quot;,&quot;New Post&quot;,null,null]">
                            <svg aria-hidden="true" class="native svg-icon iconGlyphXSm" width="18" height="18"  viewBox="0 0 18 18"><path fill="#BCBBBB" d="M14 16v-5h2v7H2v-7h2v5z"/><path fill="#F48024" d="m12.09.72-1.21.9 4.5 6.07 1.22-.9zM5 15h8v-2H5zm9.15-5.87L8.35 4.3l.96-1.16 5.8 4.83zm-7.7-1.47 6.85 3.19.63-1.37-6.85-3.2zm6.53 5L5.4 11.39l.38-1.67 7.42 1.48z"/></svg> Sign up using Email and Password
                        </div>
                    </div>
                    <input type="hidden" name="use-facebook" class="use-facebook" value="false" />
                    <input type="hidden" name="use-google" class="use-google" value="false" />
                    <button type="button" class="d-none js-submit-openid">Submit</button>
                    <div class="d-flex gsy gs8 fd-column w50 md:w-auto new-login-right form-item p0">
                                <h3 class="flex--item fs-title">Post as a guest</h3>
            <div class="flex--item">
                <div class="d-flex gs4 gsy fd-column">
                    <label class="s-label" for="display-name">Name</label>
                    <div class="d-flex ps-relative">
                        <input class="s-input" id="display-name" name="display-name" maxlength="30" type="text" value="" tabindex="105" placeholder="" />
                    </div>
                </div>
            </div>
            <div class="flex--item">
                <div class="d-flex gs4 gsy fd-column">
                    <div class="flex--item">
                        <div class="d-flex gs2 gsy fd-column">
                            <label class="flex--item s-label" for="m-address">Email</label>
                            <p class="flex--item s-description">Required, but never shown</p>
                        </div>
                    </div>
                    <div class="d-flex ps-relative">
                        <input class="s-input js-post-email-field" id="m-address" name="m-address" type="text" value="" size="40" tabindex="106" placeholder="" />
                    </div>
                </div>
            </div>

                    </div>
                </div>
            </div>
            <script>
                StackExchange.ready(
                    function () {
                        StackExchange.openid.initPostLogin('.new-post-login', 'https%3a%2f%2fstackoverflow.com%2fquestions%2f35302978%2fhow-to-get-current-value-of-androids-proximity-sensor%23new-answer', 'question_page');
                    }
                );
            </script>
            <noscript>
                        <h3 class="flex--item fs-title">Post as a guest</h3>
            <div class="flex--item">
                <div class="d-flex gs4 gsy fd-column">
                    <label class="s-label" for="display-name">Name</label>
                    <div class="d-flex ps-relative">
                        <input class="s-input" id="display-name" name="display-name" maxlength="30" type="text" value="" tabindex="105" placeholder="" />
                    </div>
                </div>
            </div>
            <div class="flex--item">
                <div class="d-flex gs4 gsy fd-column">
                    <div class="flex--item">
                        <div class="d-flex gs2 gsy fd-column">
                            <label class="flex--item s-label" for="m-address">Email</label>
                            <p class="flex--item s-description">Required, but never shown</p>
                        </div>
                    </div>
                    <div class="d-flex ps-relative">
                        <input class="s-input js-post-email-field" id="m-address" name="m-address" type="text" value="" size="40" tabindex="106" placeholder="" />
                    </div>
                </div>
            </div>

            </noscript>

                                </div>

                                    <div class="form-submit clear-both d-flex sm:fd-column sm:jc-stretch gs4 ai-center">
                                        <button id="submit-button" class="flex--item fl-shrink0 s-btn s-btn__filled sm:w100" type="submit" tabindex="120" autocomplete="off">
                                            Post Your Answer
                                        </button>
                                        <button class="flex--item s-btn s-btn__danger fl-shrink0 sm:w100 discard-answer d-none">
                                            Discard
                                        </button>
                                            <p class="flex--item mb0 fs-italic ml12 sm:ml0">
                                                By clicking “Post Your Answer”, you agree to our <a href='https://stackoverflow.com/legal/terms-of-service/public' name='tos' target='_blank' class='-link'>terms of service</a> and acknowledge you have read our <a href='https://stackoverflow.com/legal/privacy-policy' name='privacy' target='_blank' class='-link'>privacy policy</a>.<input type="hidden" name="legalLinksShown" value="1" />
                                            </p>
                                    </div>
                                    <div class="js-general-error general-error clear-both d-none" aria-live="polite"></div>
                            </form>


                            <h2 class="bottom-notice" data-loc="1">
                                <div>
Not the answer you&#x27;re looking for? Browse other questions tagged <ul class='ml0 list-ls-none js-post-tag-list-wrapper d-inline'><li class='d-inline mr4 js-post-tag-list-item'><a href="/questions/tagged/android" class="s-tag post-tag" title="show questions tagged &#39;android&#39;" aria-label="show questions tagged &#39;android&#39;" rel="tag" aria-labelledby="tag-android-tooltip-container" data-tag-menu-origin="Unknown">android</a></li><li class='d-inline mr4 js-post-tag-list-item'><a href="/questions/tagged/android-sensors" class="s-tag post-tag" title="show questions tagged &#39;android-sensors&#39;" aria-label="show questions tagged &#39;android-sensors&#39;" rel="tag" aria-labelledby="tag-android-sensors-tooltip-container" data-tag-menu-origin="Unknown">android-sensors</a></li><li class='d-inline mr4 js-post-tag-list-item'><a href="/questions/tagged/sensormanager" class="s-tag post-tag" title="show questions tagged &#39;sensormanager&#39;" aria-label="show questions tagged &#39;sensormanager&#39;" rel="tag" aria-labelledby="tag-sensormanager-tooltip-container" data-tag-menu-origin="Unknown">sensormanager</a></li><li class='d-inline mr4 js-post-tag-list-item'><a href="/questions/tagged/android-developer-api" class="s-tag post-tag" title="show questions tagged &#39;android-developer-api&#39;" aria-label="show questions tagged &#39;android-developer-api&#39;" rel="tag" aria-labelledby="tag-android-developer-api-tooltip-container" data-tag-menu-origin="Unknown">android-developer-api</a></li><li class='d-inline mr4 js-post-tag-list-item'><a href="/questions/tagged/proximitysensor" class="s-tag post-tag" title="show questions tagged &#39;proximitysensor&#39;" aria-label="show questions tagged &#39;proximitysensor&#39;" rel="tag" aria-labelledby="tag-proximitysensor-tooltip-container" data-tag-menu-origin="Unknown">proximitysensor</a></li></ul> or <a href="/questions/ask">ask your own question</a>.                                </div>
                            </h2>
                </div>
            </div>

            
<div id="sidebar" class="show-votes" role="complementary" aria-label="sidebar">
        
    <div class="sidebar-subcommunity mb16">
        <div>
                <a href="/collectives/mobile-dev/beta/discussions" class="js-gps-track" data-gps-track="subcommunity_link.click({ subcommunity_user_type: 0, subcommunity_slug: mobile-dev, link_source: 1}), subcommunity_question_discussion_widget.click({ subcommunity_user_type: 0, subcommunity_slug: mobile-dev, post_id: 35302978})">
                <span class="themed subcommunity-topic-avatar subcommunity-topic-mobile-dev bg-theme-primary btr-sm  p8 d-flex ai-center h:bs-md">
                    <span class="flex--item my6 ml4">
                        <div class="themed subcommunity-topic-avatar subcommunity-topic-mobile-dev s-avatar s-avatar__32 mr6"></div>
                    </span>
                    <span class="flex--item fl-grow1 fl-shrink0 mr8">
                        <span class="d-block fs-body2 fc-white">Mobile Development</span>
                        <span class="d-block fs-caption fc-black-150">Collective</span>
                    </span>
                    
                    <span class="s-btn s-btn__outlined s-btn__xs mr4 fc-white bc-white h:bg-theme-primary-400 f:bg-theme-primary-400">Join the discussion</span>
                </span>
            </a>
        </div>



            <div>
                <div class="fs-fine p12 ba bc-black-200 fc-black-400 bbr-sm">

                            <a href="/collectives"><svg aria-hidden="true" class="va-text-bottom svg-icon iconHelpSm" width="14" height="14"  viewBox="0 0 14 14"><path  d="M7 1C3.74 1 1 3.77 1 7c0 3.26 2.77 6 6 6 3.27 0 6-2.73 6-6s-2.73-6-6-6m1.06 9.06c-.02.63-.48 1.02-1.1 1-.57-.02-1.03-.43-1.01-1.06s.5-1.04 1.08-1.02c.6.02 1.05.45 1.03 1.08m.73-3.07-.47.3q-.31.23-.44.6a4 4 0 0 0-.08.65c0 .04-.03.14-.16.14h-1.4c-.14 0-.16-.09-.16-.13q-.02-.76.36-1.42.53-.64 1.26-1.06c.15-.1.21-.21.3-.33q.27-.32.28-.74c.01-.67-.53-1.14-1.18-1.14-.9 0-1.18.7-1.18 1.46H4.2c0-1.17.31-1.92.98-2.36a3.5 3.5 0 0 1 1.83-.44c.88 0 1.58.16 2.2.62q.88.62.88 1.82-.02.74-.43 1.24-.23.3-.86.79z"/></svg> This question is in a collective:</a> a subcommunity defined by tags with relevant content and experts.
                                        </div>
            </div>
    </div>
    <script type="text/javascript">
        StackExchange.ready(function () {
            const $showButton = $('.js-show-additional-communities');

            $showButton.on('s-expandable-control:show', function () {
                $showButton.text('Show fewer');
            });

            $showButton.on('s-expandable-control:hide', function () {
                $showButton.html($showButton.data('show-title'));
            });
        });
    </script>

    
    <div class="s-sidebarwidget s-sidebarwidget__yellow s-anchors s-anchors__grayscale mb16" data-tracker="cb=1">
            <ul class="s-sidebarwidget--content s-sidebarwidget__items p0">
                        <li class="s-sidebarwidget--header">
                            The Overflow Blog
                        </li>
        <li class="s-sidebarwidget--item d-flex px16">
            <div class="flex--item1 fl-shrink0">
<svg aria-hidden="true" class="va-text-top svg-icon iconPencilSm" width="14" height="14"  viewBox="0 0 14 14"><path fill="#F1B600" d="m2 10.12 6.37-6.43 1.88 1.88L3.88 12H2z"/><path fill="#E87C87" d="m11.1 1.71 1.13 1.12c.2.2.2.51 0 .71L11.1 4.7 9.21 2.86l1.17-1.15c.2-.2.51-.2.71 0"/></svg>            </div>
            <div class="flex--item wmn0 ow-break-word">
                <a href="https://stackoverflow.blog/2024/12/17/legal-advice-from-an-ai-is-illegal/" class="js-gps-track" data-ga="[&quot;community bulletin board&quot;,&quot;The Overflow Blog&quot;,&quot;https://stackoverflow.blog/2024/12/17/legal-advice-from-an-ai-is-illegal/&quot;,null,null]" data-gps-track="communitybulletin.click({ priority: 1, position: 0, location: questionpage })">Legal advice from an AI is illegal</a>
            </div>
        </li>
                        <li class="s-sidebarwidget--header">
                            Featured on Meta
                        </li>
        <li class="s-sidebarwidget--item d-flex px16">
            <div class="flex--item1 fl-shrink0">
<div class="favicon favicon-stackexchangemeta" title="Meta Stack Exchange"></div>            </div>
            <div class="flex--item wmn0 ow-break-word">
                <a href="https://meta.stackexchange.com/questions/404724/the-december-2024-community-asks-sprint-has-been-moved-to-march-2025-and-length" class="js-gps-track" title="The December 2024 Community Asks Sprint has been moved to March 2025 (and lengthened to 2 weeks to compensate)" data-ga="[&quot;community bulletin board&quot;,&quot;Featured on Meta&quot;,&quot;https://meta.stackexchange.com/questions/404724/the-december-2024-community-asks-sprint-has-been-moved-to-march-2025-and-length&quot;,null,null]" data-gps-track="communitybulletin.click({ priority: 3, position: 1, location: questionpage })">The December 2024 Community Asks Sprint has been moved to March 2025 (and...</a>
            </div>
        </li>
        <li class="s-sidebarwidget--item d-flex px16">
            <div class="flex--item1 fl-shrink0">
<div class="favicon favicon-stackexchangemeta" title="Meta Stack Exchange"></div>            </div>
            <div class="flex--item wmn0 ow-break-word">
                <a href="https://meta.stackexchange.com/questions/404909/stack-overflow-jobs-is-expanding-to-more-countries" class="js-gps-track" data-ga="[&quot;community bulletin board&quot;,&quot;Featured on Meta&quot;,&quot;https://meta.stackexchange.com/questions/404909/stack-overflow-jobs-is-expanding-to-more-countries&quot;,null,null]" data-gps-track="communitybulletin.click({ priority: 3, position: 2, location: questionpage })">Stack Overflow Jobs is expanding to more countries</a>
            </div>
        </li>
        </ul>
    </div>


<div class="js-zone-container zone-container-sidebar">
    <div id="dfp-tsb" class="everyonelovesstackoverflow everyoneloves__top-sidebar"></div>
		<div class="js-report-ad-button-container " style="width: 300px"></div>
</div>
<div class="js-zone-container zone-container-sidebar">
    <div id="dfp-msb" class="everyonelovesstackoverflow everyoneloves__mid-sidebar"></div>
		<div class="js-report-ad-button-container " style="width: 300px"></div>
</div>
<div id="hireme"></div>        

    


        <div class="module sidebar-related">
            <h4 id="h-related">Related</h4>
            <div class="related js-gps-related-questions" data-tracker="rq=1">
                    <div class="spacer" data-question-id="2201917">
                        <a href="/q/2201917" title="Question score (upvotes - downvotes)" >
                            <div class="answer-votes answered-accepted extra-large">1634</div>
                        </a>
                        <a href="/questions/2201917/how-can-i-open-a-url-in-androids-web-browser-from-my-application" class="question-hyperlink">How can I open a URL in Android&#39;s web browser from my application?</a>
                    </div>
                    <div class="spacer" data-question-id="937313">
                        <a href="/q/937313" title="Question score (upvotes - downvotes)" >
                            <div class="answer-votes answered-accepted extra-large">1162</div>
                        </a>
                        <a href="/questions/937313/fling-gesture-detection-on-grid-layout" class="question-hyperlink">Fling gesture detection on grid layout</a>
                    </div>
                    <div class="spacer" data-question-id="5369682">
                        <a href="/q/5369682" title="Question score (upvotes - downvotes)" >
                            <div class="answer-votes answered-accepted extra-large">1303</div>
                        </a>
                        <a href="/questions/5369682/how-to-get-current-time-and-date-in-android" class="question-hyperlink">How to get current time and date in Android</a>
                    </div>
                    <div class="spacer" data-question-id="1016896">
                        <a href="/q/1016896" title="Question score (upvotes - downvotes)" >
                            <div class="answer-votes answered-accepted extra-large">1974</div>
                        </a>
                        <a href="/questions/1016896/how-to-get-screen-dimensions-as-pixels-in-android" class="question-hyperlink">How to get screen dimensions as pixels in Android</a>
                    </div>
                    <div class="spacer" data-question-id="27373294">
                        <a href="/q/27373294" title="Question score (upvotes - downvotes)" >
                            <div class="answer-votes default">1</div>
                        </a>
                        <a href="/questions/27373294/proximity-sensor" class="question-hyperlink">Proximity Sensor</a>
                    </div>
                    <div class="spacer" data-question-id="15439405">
                        <a href="/q/15439405" title="Question score (upvotes - downvotes)" >
                            <div class="answer-votes default">0</div>
                        </a>
                        <a href="/questions/15439405/proximity-sensor-silence-call-application" class="question-hyperlink">Proximity Sensor- Silence call application</a>
                    </div>
                    <div class="spacer" data-question-id="4616095">
                        <a href="/q/4616095" title="Question score (upvotes - downvotes)" >
                            <div class="answer-votes extra-large">1602</div>
                        </a>
                        <a href="/questions/4616095/how-can-you-get-the-build-version-number-of-your-android-application" class="question-hyperlink">How can you get the build/version number of your Android application?</a>
                    </div>
                    <div class="spacer" data-question-id="16721289">
                        <a href="/q/16721289" title="Question score (upvotes - downvotes)" >
                            <div class="answer-votes answered-accepted default">3</div>
                        </a>
                        <a href="/questions/16721289/android-proximity-sensor-incorrect-value" class="question-hyperlink">Android Proximity Sensor - Incorrect value</a>
                    </div>
                    <div class="spacer" data-question-id="19650447">
                        <a href="/q/19650447" title="Question score (upvotes - downvotes)" >
                            <div class="answer-votes default">0</div>
                        </a>
                        <a href="/questions/19650447/using-proximity-sensor-in-android-4-3" class="question-hyperlink">Using Proximity Sensor in Android 4.3</a>
                    </div>
                    <div class="spacer" data-question-id="19613520">
                        <a href="/q/19613520" title="Question score (upvotes - downvotes)" >
                            <div class="answer-votes default">0</div>
                        </a>
                        <a href="/questions/19613520/actively-query-the-proximity-sensor-once" class="question-hyperlink">Actively query the proximity sensor once?</a>
                    </div>
            </div>
        </div>
        <script type="text/javascript">
                 $(function() {
                     $(".js-gps-related-questions .spacer").on("click", function () {
                        fireRelatedEvent($(this).index() + 1, $(this).data('question-id'));
                     });

                 function fireRelatedEvent(position, questionId) {
                     StackExchange.using("gps", function() {
                         StackExchange.gps.track('related_questions.click',
                         {
                             position: position,
                             originQuestionId: 35302978,
                             relatedQuestionId: +questionId,
                             location: 'sidebar',
                             source: 'Baseline_Fallback'
                         });    
                     });
                 }
             });
         </script>


    
    

    <div id="hot-network-questions" class="module tex2jax_ignore">
    <h4>
        <a href="https://stackexchange.com/questions?tab=hot"
           class="js-gps-track s-link s-link__inherit" 
           data-gps-track="posts_hot_network.click({ item_type:1, location:11 })">
            Hot Network Questions
        </a>
    </h4>
    <ul>
            <li >
                <div class="favicon favicon-english" title="English Language &amp; Usage Stack Exchange"></div><a href="https://english.stackexchange.com/questions/628084/shakespeare-and-his-syntax-we-hunt-not-we" class="js-gps-track question-hyperlink mb0" data-gps-track="site.switch({ item_type:11, target_site:97 }); posts_hot_network.click({ item_type:2, location:11 })">
                    Shakespeare and his syntax: &quot;we hunt not, we&quot;
                </a>

            </li>
            <li >
                <div class="favicon favicon-crypto" title="Cryptography Stack Exchange"></div><a href="https://crypto.stackexchange.com/questions/113793/is-there-a-way-i-can-enforce-verification-of-an-ec-signature-at-design-time-rath" class="js-gps-track question-hyperlink mb0" data-gps-track="site.switch({ item_type:11, target_site:281 }); posts_hot_network.click({ item_type:2, location:11 })">
                    Is there a way I can enforce verification of an EC signature at design-time rather than implementation-time?
                </a>

            </li>
            <li >
                <div class="favicon favicon-serverfault" title="Server Fault"></div><a href="https://serverfault.com/questions/1168972/how-to-reject-host-header-if-different-than-url-of-request-in-apache" class="js-gps-track question-hyperlink mb0" data-gps-track="site.switch({ item_type:11, target_site:2 }); posts_hot_network.click({ item_type:2, location:11 })">
                    How to reject Host header if different than URL of request in Apache?
                </a>

            </li>
            <li >
                <div class="favicon favicon-puzzling" title="Puzzling Stack Exchange"></div><a href="https://puzzling.stackexchange.com/questions/129704/pse-advent-calendar-2024-day-18-a-sweet-short-expected-chemistry-christmas" class="js-gps-track question-hyperlink mb0" data-gps-track="site.switch({ item_type:11, target_site:559 }); posts_hot_network.click({ item_type:2, location:11 })">
                    PSE Advent Calendar 2024 (Day 18): A sweet &amp; short expected chemistry Christmas puzzle
                </a>

            </li>
            <li >
                <div class="favicon favicon-tex" title="TeX - LaTeX Stack Exchange"></div><a href="https://tex.stackexchange.com/questions/733108/center-table-headers-over-certain-columns" class="js-gps-track question-hyperlink mb0" data-gps-track="site.switch({ item_type:11, target_site:85 }); posts_hot_network.click({ item_type:2, location:11 })">
                    Center table headers over certain columns
                </a>

            </li>
            <li class="dno js-hidden">
                <div class="favicon favicon-unix" title="Unix &amp; Linux Stack Exchange"></div><a href="https://unix.stackexchange.com/questions/788334/adduser-allows-weak-password-how-to-prevent" class="js-gps-track question-hyperlink mb0" data-gps-track="site.switch({ item_type:11, target_site:106 }); posts_hot_network.click({ item_type:2, location:11 })">
                    adduser allows weak password - how to prevent?
                </a>

            </li>
            <li class="dno js-hidden">
                <div class="favicon favicon-mattermodeling" title="Matter Modeling Stack Exchange"></div><a href="https://mattermodeling.stackexchange.com/questions/13841/why-is-youngs-modulus-represented-as-a-single-value-in-dft-calculations" class="js-gps-track question-hyperlink mb0" data-gps-track="site.switch({ item_type:11, target_site:704 }); posts_hot_network.click({ item_type:2, location:11 })">
                    Why is Young&#x27;s modulus represented as a single value in DFT calculations?
                </a>

            </li>
            <li class="dno js-hidden">
                <div class="favicon favicon-hermeneutics" title="Biblical Hermeneutics Stack Exchange"></div><a href="https://hermeneutics.stackexchange.com/questions/99879/is-the-book-mentioned-in-daniel-121-the-same-as-the-book-of-life-in-revelatio" class="js-gps-track question-hyperlink mb0" data-gps-track="site.switch({ item_type:11, target_site:320 }); posts_hot_network.click({ item_type:2, location:11 })">
                    Is &quot;the book&quot; mentioned in Daniel 12:1 the same as the Book of Life in Revelation?
                </a>

            </li>
            <li class="dno js-hidden">
                <div class="favicon favicon-security" title="Information Security Stack Exchange"></div><a href="https://security.stackexchange.com/questions/279900/immutable-backups-an-important-protection-against-ransomware-or-yet-another-m" class="js-gps-track question-hyperlink mb0" data-gps-track="site.switch({ item_type:11, target_site:162 }); posts_hot_network.click({ item_type:2, location:11 })">
                    &quot;Immutable backups&quot;: an important protection against ransomware or yet another marketing product?
                </a>

            </li>
            <li class="dno js-hidden">
                <div class="favicon favicon-english" title="English Language &amp; Usage Stack Exchange"></div><a href="https://english.stackexchange.com/questions/628052/is-there-an-english-equivalent-of-arabic-gowatra-performing-a-task-with-none" class="js-gps-track question-hyperlink mb0" data-gps-track="site.switch({ item_type:11, target_site:97 }); posts_hot_network.click({ item_type:2, location:11 })">
                    Is there an English equivalent of Arabic &quot;gowatra&quot; - performing a task with none of the necessary training?
                </a>

            </li>
            <li class="dno js-hidden">
                <div class="favicon favicon-academia" title="Academia Stack Exchange"></div><a href="https://academia.stackexchange.com/questions/215547/how-to-interpret-being-told-that-there-are-no-current-phd-openings-but-i-should" class="js-gps-track question-hyperlink mb0" data-gps-track="site.switch({ item_type:11, target_site:415 }); posts_hot_network.click({ item_type:2, location:11 })">
                    How to interpret being told that there are no current PhD openings but I should &quot;keep in touch&quot; for potential future opportunities?
                </a>

            </li>
            <li class="dno js-hidden">
                <div class="favicon favicon-hermeneutics" title="Biblical Hermeneutics Stack Exchange"></div><a href="https://hermeneutics.stackexchange.com/questions/99890/why-the-serpent-was-more-crafty-than-any-of-the-wild-animals-the-lord-god-made" class="js-gps-track question-hyperlink mb0" data-gps-track="site.switch({ item_type:11, target_site:320 }); posts_hot_network.click({ item_type:2, location:11 })">
                    Why the serpent was more crafty than any of the wild animals the Lord God made?
                </a>

            </li>
            <li class="dno js-hidden">
                <div class="favicon favicon-codereview" title="Code Review Stack Exchange"></div><a href="https://codereview.stackexchange.com/questions/294748/polymorphic-message-container" class="js-gps-track question-hyperlink mb0" data-gps-track="site.switch({ item_type:11, target_site:196 }); posts_hot_network.click({ item_type:2, location:11 })">
                    polymorphic message container
                </a>

            </li>
            <li class="dno js-hidden">
                <div class="favicon favicon-puzzling" title="Puzzling Stack Exchange"></div><a href="https://puzzling.stackexchange.com/questions/129690/pse-advent-calendar-2024-day-17-the-sun-will-come-out-tomorrow" class="js-gps-track question-hyperlink mb0" data-gps-track="site.switch({ item_type:11, target_site:559 }); posts_hot_network.click({ item_type:2, location:11 })">
                    PSE Advent Calendar 2024 (Day 17): The Sun Will Come Out Tomorrow
                </a>

            </li>
            <li class="dno js-hidden">
                <div class="favicon favicon-hermeneutics" title="Biblical Hermeneutics Stack Exchange"></div><a href="https://hermeneutics.stackexchange.com/questions/99903/do-the-jews-recognize-abraham-to-david-as-14-generations-i-know-matthews-gospe" class="js-gps-track question-hyperlink mb0" data-gps-track="site.switch({ item_type:11, target_site:320 }); posts_hot_network.click({ item_type:2, location:11 })">
                    Do the Jews recognize Abraham to David as 14 generations? I know Matthew&#x27;s gospel makes the point, but did Jews (before Matt) make mention of 14 gen?
                </a>

            </li>
            <li class="dno js-hidden">
                <div class="favicon favicon-physics" title="Physics Stack Exchange"></div><a href="https://physics.stackexchange.com/questions/837501/are-there-actual-correct-representations-of-curved-spacetime" class="js-gps-track question-hyperlink mb0" data-gps-track="site.switch({ item_type:11, target_site:151 }); posts_hot_network.click({ item_type:2, location:11 })">
                    Are there actual correct representations of curved spacetime?
                </a>

            </li>
            <li class="dno js-hidden">
                <div class="favicon favicon-literature" title="Literature Stack Exchange"></div><a href="https://literature.stackexchange.com/questions/28371/why-does-david-copperfield-say-he-is-born-on-a-friday-rather-than-a-saturday" class="js-gps-track question-hyperlink mb0" data-gps-track="site.switch({ item_type:11, target_site:668 }); posts_hot_network.click({ item_type:2, location:11 })">
                    Why does David Copperfield say he is born on a Friday rather than a Saturday?
                </a>

            </li>
            <li class="dno js-hidden">
                <div class="favicon favicon-diy" title="Home Improvement Stack Exchange"></div><a href="https://diy.stackexchange.com/questions/311783/why-am-i-not-seeing-continuity-between-mc-cable-sheathing-and-ground-wires" class="js-gps-track question-hyperlink mb0" data-gps-track="site.switch({ item_type:11, target_site:73 }); posts_hot_network.click({ item_type:2, location:11 })">
                    Why am I not seeing continuity between MC cable sheathing and ground wires?
                </a>

            </li>
            <li class="dno js-hidden">
                <div class="favicon favicon-askubuntu" title="Ask Ubuntu"></div><a href="https://askubuntu.com/questions/1535882/clone-kubuntu-to-different-computer-different-hardware" class="js-gps-track question-hyperlink mb0" data-gps-track="site.switch({ item_type:11, target_site:89 }); posts_hot_network.click({ item_type:2, location:11 })">
                    Clone Kubuntu to different computer, different hardware
                </a>

            </li>
            <li class="dno js-hidden">
                <div class="favicon favicon-tex" title="TeX - LaTeX Stack Exchange"></div><a href="https://tex.stackexchange.com/questions/733096/center-text-in-a-cell" class="js-gps-track question-hyperlink mb0" data-gps-track="site.switch({ item_type:11, target_site:85 }); posts_hot_network.click({ item_type:2, location:11 })">
                    Center text in a cell
                </a>

            </li>
            <li class="dno js-hidden">
                <div class="favicon favicon-mathematica" title="Mathematica Stack Exchange"></div><a href="https://mathematica.stackexchange.com/questions/309454/joining-two-lists-by-matching-elements-of-the-two" class="js-gps-track question-hyperlink mb0" data-gps-track="site.switch({ item_type:11, target_site:387 }); posts_hot_network.click({ item_type:2, location:11 })">
                    Joining two lists by matching elements of the two
                </a>

            </li>
            <li class="dno js-hidden">
                <div class="favicon favicon-puzzling" title="Puzzling Stack Exchange"></div><a href="https://puzzling.stackexchange.com/questions/129685/a-sad-looking-tree-with-a-secret" class="js-gps-track question-hyperlink mb0" data-gps-track="site.switch({ item_type:11, target_site:559 }); posts_hot_network.click({ item_type:2, location:11 })">
                    A sad-looking tree with a secret
                </a>

            </li>
            <li class="dno js-hidden">
                <div class="favicon favicon-stats" title="Cross Validated"></div><a href="https://stats.stackexchange.com/questions/658909/what-should-the-objective-be-when-tuning-hyperparameters-to-minimize-overfitting" class="js-gps-track question-hyperlink mb0" data-gps-track="site.switch({ item_type:11, target_site:65 }); posts_hot_network.click({ item_type:2, location:11 })">
                    What should the objective be when tuning hyperparameters to minimize overfitting?
                </a>

            </li>
            <li class="dno js-hidden">
                <div class="favicon favicon-scifi" title="Science Fiction &amp; Fantasy Stack Exchange"></div><a href="https://scifi.stackexchange.com/questions/293669/brain-ship-eats-hijacker" class="js-gps-track question-hyperlink mb0" data-gps-track="site.switch({ item_type:11, target_site:186 }); posts_hot_network.click({ item_type:2, location:11 })">
                    Brain ship &#x27;eats&#x27; hijacker
                </a>

            </li>
    </ul>

        <a href="#" 
           class="show-more js-show-more js-gps-track" 
           data-gps-track="posts_hot_network.click({ item_type:3, location:11 })">
            more hot questions
        </a>
</div>

                <div id="feed-link" class="js-feed-link">
        <a href="/feeds/question/35302978" title="Feed of this question and its answers">
            <svg aria-hidden="true" class="fc-orange-400 svg-icon iconRss" width="18" height="18"  viewBox="0 0 18 18"><path  d="M3 1a2 2 0 0 0-2 2v12c0 1.1.9 2 2 2h12a2 2 0 0 0 2-2V3a2 2 0 0 0-2-2zm0 1.5c6.9 0 12.5 5.6 12.5 12.5H13C13 9.55 8.45 5 3 5zm0 5c4.09 0 7.5 3.41 7.5 7.5H8c0-2.72-2.28-5-5-5zm0 5c1.36 0 2.5 1.14 2.5 2.5H3z"/></svg>
            Question feed
        </a>
    </div>
    <aside class="s-modal js-feed-link-modal" tabindex="-1" role="dialog" aria-labelledby="feed-modal-title" aria-describedby="feed-modal-description" aria-hidden="true">
        <div class="s-modal--dialog js-modal-dialog wmx4" role="document"  data-controller="se-draggable">
            <h1 class="s-modal--header fw-bold js-first-tabbable" id="feed-modal-title" data-se-draggable-target="handle" tabindex="0">
                Subscribe to RSS
            </h1>
            <div class="d-flex gs4 gsy fd-column">
                <div class="flex--item">
                    <label class="d-block s-label c-default" for="feed-url">
                        Question feed
                        <p class="s-description mt2" id="feed-modal-description">To subscribe to this RSS feed, copy and paste this URL into your RSS reader.</p>
                    </label>
                </div>
                <div class="d-flex ps-relative">
                    <input class="s-input" type="text" name="feed-url" id="feed-url" readonly="readonly" value="https://stackoverflow.com/feeds/question/35302978" />
                    <svg aria-hidden="true" class="s-input-icon fc-orange-400 svg-icon iconRss" width="18" height="18"  viewBox="0 0 18 18"><path  d="M3 1a2 2 0 0 0-2 2v12c0 1.1.9 2 2 2h12a2 2 0 0 0 2-2V3a2 2 0 0 0-2-2zm0 1.5c6.9 0 12.5 5.6 12.5 12.5H13C13 9.55 8.45 5 3 5zm0 5c4.09 0 7.5 3.41 7.5 7.5H8c0-2.72-2.28-5-5-5zm0 5c1.36 0 2.5 1.14 2.5 2.5H3z"/></svg>
                </div>
            </div>
            <a class="s-modal--close s-btn s-btn__muted js-modal-close js-last-tabbable" href="#" aria-label="Close">
                <svg aria-hidden="true" class="svg-icon iconClearSm" width="14" height="14"  viewBox="0 0 14 14"><path  d="M12 3.41 10.59 2 7 5.59 3.41 2 2 3.41 5.59 7 2 10.59 3.41 12 7 8.41 10.59 12 12 10.59 8.41 7z"/></svg>
            </a>
        </div>
    </aside>

</div>

    </div>
<script>StackExchange.ready(function(){$.get('/posts/35302978/ivc/5375?prg=7622944e-81f5-4ffb-a866-9de0381416ff');});</script>
<noscript><div><img src="/posts/35302978/ivc/5375?prg=7622944e-81f5-4ffb-a866-9de0381416ff" class="dno" alt="" width="0" height="0"></div></noscript><div style="display:none" id="js-codeblock-lang">default</div></div>


<script>console.error(`Unable to load nonexistent manifest entry 'recent-posts'. Check that your file path is correct.`)</script>

                        


        </div>
    </div>

    

        
    <script type="text/javascript">
    var cam = cam || { opt: {} };
    var clcGamLoaderOptions = cam || { opt: {} };
    var opt = clcGamLoaderOptions.opt;

    opt.omni = 'BwoLCNrmz8bO_M89EAUYwtzqECACKAI6TXxhbmRyb2lkfGFuZHJvaWQtc2Vuc29yc3xzZW5zb3JtYW5hZ2VyfGFuZHJvaWQtZGV2ZWxvcGVyLWFwaXxwcm94aW1pdHlzZW5zb3J8QAFIAVoSCfB8B555YpdFEYVaHsdNYZ9lTJr4isplccN4ow';
    opt.refresh = !1;
    opt.refreshInterval = 90;
    opt.sf = !0;
    opt.hb = !1;
    opt.ll = !0;
    opt.tlb_position = 0;
    opt.personalization_consent = !0;
    opt.targeting_consent = !0;
    opt.performance_consent = !0;

    opt.targeting = {Registered:['false'],Reputation:['new'],'so-tag':['android','android-sensors','sensormanager','android-developer-api','proximitysensor'],'tag-reportable':['android','android-sensors','sensormanager','android-developer-api','proximitysensor'],'so_tag':['android','android_sensors','sensormanager','android_developer_api','proximitysensor'],NumberOfAnswers:['2'],'Collectives':['mobile_dev'],cf_bot_score:'61 - 80'};
    opt.adReportEnabled = !0;
    opt.adReportUrl = '/ads/report-ad';
    opt.adReportText = 'Report this ad';
	opt.adReportFileTypeErrorMessage = 'Please select a PNG or JPG file.';
    opt.adReportFileSizeErrorMessage = 'The file must be under 2 MiB.';
	opt.adReportErrorText = 'Error uploading ad report.';
	opt.adReportThanksText = 'Thanks for your feedback. We’ll review this against our code of conduct and take action if necessary.';
    opt.adReportLoginExpiredMessage = 'Your login session has expired, please login and try again.';
    opt.adReportLoginErrorMessage = 'An error occurred when loading the report form - please try again';
	opt.adReportModalClass = 'js-ad-report';
    opt.countryCode = 'HK';
    opt.qualtricsSurveyData = '{"isRegistered":"False","repBucket":"new","referrer":"https%3a%2f%2fstackoverflow.com%2fquestions%2f35302978%2fhow-to-get-current-value-of-androids-proximity-sensor","accountAge":"0"}';

        opt.brandSurveyEnabled = true;
            opt.brandSurveySettings = [{"brandId":7,"lineItemIds":[6170355049,6170355058,6170355244,6168829383,6170355787,6170355799,6168829803,6170356261,6170356282,6170984786,6170985065,6168833181,6170358871,6170360326,6170360578,6168834204,6170361016,6170986253,6377604184,6378262502,6378262511,6377604211,6377604223,6377604700,6318450889,6318453241,6318453259,6318453310],"mode":"Collect"},{"brandId":8,"lineItemIds":[6389119380,6389119404,6389119347],"mode":"Collect"},{"brandId":9,"lineItemIds":[6695878301,6695879039,6695879168,6695879174,6695879186],"mode":"Collect"},{"brandId":10,"lineItemIds":[6456294147,6456294228,6456294381,6456294396,6456294633,6456294714,6456294906,6458534116,6458539435,6458540062,6459217607,6459218636,6459219038,6459219551,6458539678,6458539864,6458539918,6459217100,6459218396,6459218846,6459219500,6459219983,6456293469,6456293664,6456293949,6459216860,6459217889,6459217904,6459218117,6459218306],"mode":"Collect"}];
    opt.perRequestGuid = '7622944e-81f5-4ffb-a866-9de0381416ff';
    opt.responseHash = '3Lq3Fqhbm7rX0k&#x2B;z5b7AijMI6UFkBQVmhz2alRKW1XY=';


    opt.targeting.TargetingConsent = ['True'];
    opt.allowAccountTargetingForThisRequest = !1;

    const urlParams = new URLSearchParams(window.location.search);
    if (urlParams.has('dfptestads')) {
        const dfptestads = urlParams.get('dfptestads');
        opt.targeting.DfpTestAds = dfptestads;
    }
</script>
<script>;(()=>{"use strict";var __webpack_modules__={23:(e,t,s)=>{s.d(t,{Z7:()=>c,eq:()=>l,kG:()=>d});const n="248424177",o=(a=location.pathname,/^\/tags\//.test(a)||/^\/questions\/tagged\//.test(a)?"tag-pages":/^\/discussions\//.test(a)||/^\/beta\/discussions/.test(a)?"discussions":/^\/$/.test(a)||/^\/home/.test(a)?"home-page":/^\/jobs$/.test(a)||/^\/jobs\//.test(a)?"jobs":"question-pages");var a;let i=location.hostname;const r={slots:{lb:[[728,90]],mlb:[[728,90]],smlb:[[728,90]],bmlb:[[728,90]],sb:e=>"dfp-tsb"===e?[[300,250],[300,600]]:[[300,250]],"tag-sponsorship":[[730,135]],"mobile-below-question":[[320,50],[300,250]],msb:[[300,250],[300,600]],"talent-conversion-tracking":[[1,1]],"site-sponsorship":[[230,60]]},ids:{"dfp-tlb":"lb","dfp-mlb":"mlb","dfp-smlb":"smlb","dfp-bmlb":"bmlb","dfp-tsb":"sb","dfp-isb":"sb","dfp-tag":"tag-sponsorship","dfp-msb":"msb","dfp-sspon":"site-sponsorship","dfp-m-aq":"mobile-below-question"},idsToExcludeFromAdReports:["dfp-sspon"]};function d(){return Object.keys(r.ids)}function l(e){return r.idsToExcludeFromAdReports.indexOf(e)<0}function c(e){var t=e.split("_")[0];const s=r.ids[t];let a=r.slots[s];return"function"==typeof a&&(a=a(t)),{path:`/${n}/${i}/${s}/${o}`,sizes:a,zone:s}}},865:(e,t,s)=>{function n(e){return"string"==typeof e?document.getElementById(e):e}function o(e){return!!(e=n(e))&&"none"===getComputedStyle(e).display}function a(e){return!o(e)}function i(e){return!!e}function r(e){return/^\s*$/.test(n(e).innerHTML)}function d(e){const{style:t}=e;t.height=t.maxHeight=t.minHeight="auto",t.display="none"}function l(e){const{style:t}=e;t.height=t.maxHeight=t.minHeight="auto",t.display="none",[].forEach.call(e.children,l)}function c(e){const{style:t}=e;t.height=t.maxHeight=t.minHeight="auto",t.removeProperty("display")}function g(e){const t=document.createElement("script");t.src=e,document.body.appendChild(t)}function p(e){return s=e,(t=[]).push=function(e){return s(),delete this.push,this.push(e)},t;var t,s}function h(e){let t="function"==typeof HTMLTemplateElement;var s=document.createElement(t?"template":"div");return e=e.trim(),s.innerHTML=e,t?s.content.firstChild:s.firstChild}s.d(t,{$Z:()=>c,Bv:()=>h,Gx:()=>g,Nj:()=>n,QZ:()=>p,cf:()=>d,pn:()=>a,wo:()=>l,xb:()=>r,xj:()=>o,yb:()=>i})},763:(__unused_webpack_module,__webpack_exports__,__webpack_require__)=>{__webpack_require__.d(__webpack_exports__,{t:()=>AdReports});var _common_helper__WEBPACK_IMPORTED_MODULE_2__=__webpack_require__(865),_console__WEBPACK_IMPORTED_MODULE_1__=__webpack_require__(276),_ad_units__WEBPACK_IMPORTED_MODULE_0__=__webpack_require__(23);class AdReports{constructor(e,t){if(this.googletag=e,this.cam=t,this.allowedFileTypes=["image/png","image/jpg","image/jpeg"],this.ignoreValidation=!1,_console__WEBPACK_IMPORTED_MODULE_1__.cM("Ad reporting init"),this.cam=t,this.callOnButtonClick=e=>this.onButtonClick(e),this.googletag.pubads().addEventListener("slotRenderEnded",e=>this.handleSlotRendered(e)),Array.isArray(t.slotsRenderedEvents)){_console__WEBPACK_IMPORTED_MODULE_1__.cM("Adding report button to "+t.slotsRenderedEvents.length+" events that have transpired");for(var s=0;s<t.slotsRenderedEvents.length;s++)this.handleSlotRendered(t.slotsRenderedEvents[s])}}handleSlotRendered(e){if(e&&e.slot&&!e.isEmpty&&(e.creativeId||e.lineItemId||!e.isEmpty)){var t=e.slot.getSlotElementId();if(t){var s=document.getElementById(t);if(s)if((0,_ad_units__WEBPACK_IMPORTED_MODULE_0__.eq)(t)){var n=s?.closest(".js-zone-container")?.querySelector(".js-report-ad-button-container");n?(n.innerHTML="",n.append(this.createButton(e)),n.style.height="24px",_console__WEBPACK_IMPORTED_MODULE_1__.cM("Added report button to the bottom of "+t)):_console__WEBPACK_IMPORTED_MODULE_1__.cM("Ad report button not found, may be intentional, element: "+t)}else _console__WEBPACK_IMPORTED_MODULE_1__.cM("Not adding report button to the bottom of "+t+": shouldHaveReportButton = false");else _console__WEBPACK_IMPORTED_MODULE_1__.cM("Not adding report button to the bottom of "+t+": resolved invalid adUnit element")}else _console__WEBPACK_IMPORTED_MODULE_1__.cM("Not adding report button to the bottom of element: invalid adUnitElementId")}else _console__WEBPACK_IMPORTED_MODULE_1__.cM("Not adding report button to the bottom of element: invalid SlotRenderEndedEvent")}async onButtonClick(e){e.preventDefault();let t=e.target;const s=t.dataset.modalUrl,n=t.dataset.googleEventData;return await this.loadModal(s,t,n),!1}createButton(e){let t=document.createElement("button");var s=JSON.stringify(e);return t.dataset.googleEventData=s,t.dataset.modalUrl=this.cam.opt.adReportUrl,t.dataset.adUnit=e.slot.getSlotElementId(),t.classList.add("js-report-ad","s-btn","s-btn__link","fs-fine","mt2","float-right"),t.append(document.createTextNode(this.cam.opt.adReportText)),t.removeEventListener("click",this.callOnButtonClick),t.addEventListener("click",this.callOnButtonClick),t}async loadModal(url,$link,googleEventData){try{await window.StackExchange.helpers.loadModal(url,{returnElements:window.$($link)}),this.initForm(googleEventData)}catch(e){var message="",response=e.responseText?eval(`(${e.responseText})`):null;message=response&&response.isLoggedOut?this.cam.opt.adReportLoginExpiredMessage:this.cam.opt.adReportLoginErrorMessage,window.StackExchange.helpers.showToast(message,{type:"danger"})}}removeModal(){window.StackExchange.helpers.closePopups(document.querySelectorAll("."+this.cam.opt.adReportModalClass),"dismiss")}initForm(e,t=!1){this.ignoreValidation=t,this.$form=document.querySelector(".js-ad-report-form"),this.$googleEventData=this.$form.querySelector(".js-json-data"),this.$adReportReasons=this.$form.querySelectorAll(".js-ad-report-reason"),this.$adReportReasonOther=this.$form.querySelector(".js-ad-report-reason-other"),this.$fileUploaderInput=this.$form.querySelector(".js-file-uploader-input"),this.$imageUploader=this.$form.querySelector(".js-image-uploader"),this.$clearImageUpload=this.$form.querySelector(".js-clear-image-upload"),this.$imageUploaderText=this.$form.querySelector(".js-image-uploader-text"),this.$imageUploaderPreview=this.$form.querySelector(".js-image-uploader-preview"),this.$fileErrorMessage=this.$form.querySelector(".js-file-error");const s=this.$form.querySelector(".js-drag-drop-enabled"),n=this.$form.querySelector(".js-drag-drop-disabled");this.$googleEventData.value=e,this.$adReportReasons.forEach((e,t)=>e.addEventListener("change",e=>{this.$adReportReasonOther.classList.toggle("d-none","3"!==e.target.value)})),this.$fileUploaderInput.addEventListener("change",()=>{this.validateFileInput()&&this.updateImagePreview(this.$fileUploaderInput.files)}),this.$clearImageUpload.addEventListener("click",e=>{e.preventDefault(),this.clearImageUpload()});try{this.$fileUploaderInput[0].value="",this.$imageUploader.addEventListener("dragenter dragover dragleave drop",this.preventDefaults),this.$imageUploader.addEventListener("dragenter dragover",this.handleDragStart),this.$imageUploader.addEventListener("dragleave drop",this.handleDragEnd),this.$imageUploader.addEventListener("drop",this.handleDrop)}catch(e){s.classList.add("d-none"),n.classList.remove("d-none")}this.$form.removeEventListener("",this.handleDragEnd),this.$form.addEventListener("submit",async e=>(e.preventDefault(),this.submitForm(),!1))}clearImageUpload(){this.$fileUploaderInput.value="",this.$imageUploaderPreview.setAttribute("src",""),this.$imageUploaderPreview.classList.add("d-none"),this.$clearImageUpload.classList.add("d-none"),this.$imageUploaderText.classList.remove("d-none"),this.$imageUploader.classList.add("p16","ba","bas-dashed","bc-black-100")}preventDefaults(e){e.preventDefault(),e.stopPropagation()}handleDragStart(e){this.$imageUploader.classList.remove("bas-dashed"),this.$imageUploader.classList.add("bas-solid","bc-black-100")}handleDragEnd(e){this.$imageUploader.classList.remove("bas-solid","bc-black-100"),this.$imageUploader.classList.add("bas-dashed")}handleDrop(e){var t=e.originalEvent.dataTransfer.files;FileReader&&t&&1===t.length&&(this.$fileUploaderInput.files=t,this.validateFileInput()&&this.updateImagePreview(t))}setError(e){this.$fileErrorMessage.parentElement.classList.toggle("has-error",e)}updateImagePreview(e){this.$imageUploader.classList.remove("p16","ba","bas-dashed","bc-black-100"),this.$clearImageUpload.classList.remove("d-none"),this.$imageUploaderText.classList.add("d-none");var t=new FileReader;t.onload=e=>{null!=e.target&&(this.$imageUploaderPreview.setAttribute("src",e.target.result),this.$imageUploaderPreview.classList.remove("d-none"))},t.readAsDataURL(e[0])}validateFileInput(){if(this.ignoreValidation)return!0;const e=this.cam.opt.adReportFileTypeErrorMessage,t=this.cam.opt.adReportFileSizeErrorMessage;if(null==this.$fileUploaderInput.files)return!1;var s=this.$fileUploaderInput.files[0];return null==s?(this.setError(!0),!1):this.allowedFileTypes.indexOf(s.type)<0?(this.$fileErrorMessage.textContent=e,this.$fileErrorMessage.classList.remove("d-none"),this.setError(!0),!1):s.size>2097152?(this.$fileErrorMessage.textContent=t,this.$fileErrorMessage.classList.remove("d-none"),this.setError(!0),!1):(this.$fileErrorMessage.classList.add("d-none"),this.setError(!1),!0)}async gatherDiagnosticInfo(){return{BrowserVersion:await this.getBrowserVersion()}}getElementSource(e){return e.outerHTML}getNestedIFrameElement(e){var t=e.querySelector("iframe");return t.contentDocument?t.contentDocument.documentElement:t.contentWindow.document.documentElement}async getBrowserVersion(){return await navigator.userAgentData.getHighEntropyValues(["fullVersionList"]).then(e=>JSON.stringify(e.fullVersionList))}async submitForm(){if(!this.validateFileInput())return!1;this.$form.querySelector("[type=submit]").setAttribute("disabled","true");var e=JSON.parse(this.$googleEventData.value||"{}");e.Reason=parseInt(this.$form.querySelector(".js-ad-report-reason:checked").value,10),e.Description=this.$adReportReasonOther.value,this.$googleEventData.value=JSON.stringify(e);var t=new FormData(this.$form);if("1"===t.get("shareDiagnosticInfo")){var s=await this.gatherDiagnosticInfo();Object.keys(s).forEach(e=>t.append(e,s[e]))}try{const e=await window.fetch(this.$form.getAttribute("action"),{method:this.$form.getAttribute("method"),body:t,cache:"no-cache"}),s=e.headers.get("content-type")||"",o=await e.text();if(!e.ok)throw new Error("response not valid");if(0===s.indexOf("text/html")){var n=(0,_common_helper__WEBPACK_IMPORTED_MODULE_2__.Bv)(o);const e=n?n.querySelector(".js-modal-content"):null;if(_console__WEBPACK_IMPORTED_MODULE_1__.cM("$popupContent"),_console__WEBPACK_IMPORTED_MODULE_1__.cM(e),!e)throw new Error(`Could not find .js-modal-content in response from ${this.$form.getAttribute("action")}`);document.querySelector(".js-modal-content").replaceWith(e)}else window.StackExchange.helpers.showToast(this.cam.opt.adReportThanksText,{type:"success"}),this.removeModal()}catch(e){window.StackExchange.helpers.showToast(this.cam.opt.adReportErrorText,{type:"danger"})}finally{let e=this.$form.querySelector("[type=submit]");e&&e.removeAttribute("disabled")}}}},276:(e,t,s)=>{function n(...e){}function o(...e){}s.d(t,{cM:()=>n,vU:()=>o})}},__webpack_module_cache__={};function __webpack_require__(e){var t=__webpack_module_cache__[e];if(void 0!==t)return t.exports;var s=__webpack_module_cache__[e]={exports:{}};return __webpack_modules__[e](s,s.exports,__webpack_require__),s.exports}__webpack_require__.d=(e,t)=>{for(var s in t)__webpack_require__.o(t,s)&&!__webpack_require__.o(e,s)&&Object.defineProperty(e,s,{enumerable:!0,get:t[s]})},__webpack_require__.o=(e,t)=>Object.prototype.hasOwnProperty.call(e,t);var __webpack_exports__={};(()=>{var e=__webpack_require__(276),t=(e=>(e[e.Above=0]="Above",e[e.Below=1]="Below",e))(t||{});const s=Object.assign({},{"lib":"https://clc.stackoverflow.com/Content/bundles/js/gam_loader_script.bundle.741.25e3e63be9a306287d9f.js?v=d5f908ccaade","style":null,"u":null,"wa":true,"kt":2000,"tto":true,"h":"clc.stackoverflow.com","allowed":"^(((talent\\.)?stackoverflow)|(blog\\.codinghorror)|(.*\\.googlesyndication)|(serverfault|askubuntu|superuser)|([^\\.]+\\.stackexchange))\\.com$","wv":true,"al":false,"abd":true,"cpa_liid":[5882654614],"cpa_cid":[138377597667],"dp":false,"tgt_to":1000,"tgt_u":"https://clc.stackoverflow.com/get-user-acct-tgt","tgt_e":true,"tgt_p":100,"dv_enabled":false});var n=__webpack_require__(23),o=__webpack_require__(865),a=__webpack_require__(763);class i{constructor(t,s){this.googletag=t,this.interval=s,e.cM("Ad refresh init. interval: "+s),this.googletag.pubads().addEventListener("impressionViewable",e=>this.onImpressionViewable(e)),e.cM("done enabling ad refresh")}onImpressionViewable(t){var s=t.slot;e.cM("ad refresh - slot "+s.getSlotElementId()+" is viewable, initializing refresh"),this.scheduleRefresh(s)}scheduleRefresh(e){setTimeout(()=>this.refreshAdSlot(e),1e3*this.interval)}static refreshMyAd(t,s){let n=t.pubads().getSlots().find(e=>e.getSlotElementId()===s);n&&(e.cM("refreshMyAd - refreshing ad slot "+s),t.pubads().refresh([n]))}static removeMyAd(t,s){let n=t.pubads().getSlots().find(e=>e.getSlotElementId()===s);n&&(e.cM("removeMyAd - destroying ad slot "+s),t.destroySlots([n]))}refreshAdSlot(t){var s=t.getSlotElementId();this.isElementVisibleInBrowser(s)?(e.cM("refreshing ad slot "+s),googletag.pubads().refresh([t])):(e.cM("refresh skipped this time; ad slot not viewable:"+s),this.scheduleRefresh(t))}isElementVisibleInBrowser(e){var t=document.getElementById(e);if(null!==t){var s=t.getBoundingClientRect();if(s.top>=0&&s.left>=0&&s.bottom<=(window.innerHeight||document.documentElement.clientHeight)&&s.right<=(window.innerWidth||document.documentElement.clientWidth))return!0}return!1}}var r=(e=>(e.Off="Off",e.PreSurvey="PreSurvey",e.Collect="Collect",e.PostSurvey="PostSurvey",e))(r||{});class d{constructor(e,t){this.lineItemImpressions=[],this.surveysIdsCompleted=[],this.lineItemImpressions=e,this.surveysIdsCompleted=t}addImpression(e,t){let s={brandId:e,lineItemId:t,timestamp:new Date};this.lineItemImpressions.push(s)}addBrandSurveyCompleted(e){-1===this.surveysIdsCompleted.indexOf(e)&&this.surveysIdsCompleted.push(e)}getTotalBrandImpressions(){let e=new Map;for(let t of this.lineItemImpressions)if(e.has(t.brandId)){let s=e.get(t.brandId);e.set(t.brandId,s+1)}else e.set(t.brandId,1);return e}getBrandLineItemImpressions(e){let t={};for(let s of this.lineItemImpressions)if(s.brandId==e)if(void 0!==t[s.lineItemId]){let e=t[s.lineItemId];t[s.lineItemId]=e+1}else t[s.lineItemId]=1;return t}}class l{constructor(){this.surveyEngagementLocalStorageKey="clc-survey-engagement"}getBrandSurveyEngagement(){let e=localStorage.getItem(this.surveyEngagementLocalStorageKey);if(null===e)return new d([],[]);let t=JSON.parse(e);return new d(t.lineItemImpressions,t.surveysIdsCompleted)}saveBrandSurveyEngagement(e){let t=JSON.stringify(e);localStorage.setItem(this.surveyEngagementLocalStorageKey,t)}}class c{constructor(){this.surveyRepository=new l}getBrandSurveyEngagement(){return this.surveyRepository.getBrandSurveyEngagement()}recordImpression(e,t){let s=this.getBrandSurveyEngagement();s.addImpression(e,t),this.surveyRepository.saveBrandSurveyEngagement(s)}recordBrandSurveyCompleted(e){let t=this.getBrandSurveyEngagement();t.addBrandSurveyCompleted(e),this.surveyRepository.saveBrandSurveyEngagement(t)}}class g{constructor(t,s){this.googletag=t,this.brandSettings=s,this.brandSlotMap=new Map,this.brandSurveyEngagementService=new c,e.cM("Brand Survey init: "+JSON.stringify(s)),void 0!==s?(this.googletag.pubads().addEventListener("slotRenderEnded",e=>this.handleSlotRendered(e)),this.googletag.pubads().addEventListener("impressionViewable",e=>this.onImpressionViewable(e)),e.cM("done enabling Brand Survey")):e.cM("Brand Survey init: brandSettings is undefined, not initializing")}handleSlotRendered(t){e.cM("Brand Survey - slot rendered - slot:"+JSON.stringify(t.slot.getSlotElementId())+" lineItem: "+t.lineItemId);let s=this.findItemWithId(t.lineItemId);if(null===s||s.mode!==r.Collect)this.brandSlotMap.delete(t.slot.getSlotElementId());else{let e={brandId:s.brandId,lineItemId:t.lineItemId};this.brandSlotMap.set(t.slot.getSlotElementId(),e)}}onImpressionViewable(t){let s=t.slot;if(e.cM("ad - Brand Survey - impression viewable.  Details: "+JSON.stringify(s.getSlotElementId())),e.cM("ad - Brand Survey - slot "+s.getSlotElementId()+" is viewable"),this.brandSlotMap.has(s.getSlotElementId())){let t=this.brandSlotMap.get(s.getSlotElementId());e.cM("Brand Survey - brand "+t.brandId+" is viewable"),this.recordImpression(this.brandSlotMap.get(s.getSlotElementId()))}}recordImpression(t){e.cM("ad - Brand Survey - recording impression for brand "+t.brandId),this.brandSurveyEngagementService.recordImpression(t.brandId,t.lineItemId)}findItemWithId(t){return e.cM("brand settings: "+JSON.stringify(this.brandSettings)),this.brandSettings.find(e=>e.lineItemIds.includes(t))||null}}const p="response-brand-survey-submit|",h="request-brand-survey-metadata|",m="record-metric-on-server|",u="request-dsp-tags",f="response-dsp-tags|";class v{static refreshAdIfBrandSurveyIsDuplicated(e,t,s){if(this.alreadyCompletedThisBrandSurvey(t)){var n=document.getElementById(s).closest(".js-zone-container");i.removeMyAd(e,s),n&&n.remove()}}static alreadyCompletedThisBrandSurvey(e){return(new c).getBrandSurveyEngagement().surveysIdsCompleted.includes(e)}}window.cam=new class{constructor(t=null){if(this.gptImported=!1,this.slotsRenderedEvents=[],this.collapsed={},e.cM("constructor"),this.clc_options=s,window.clcGamLoaderOptions)Object.assign(this,window.clcGamLoaderOptions);else if(void 0===this.opt){let e=window.opt;e&&(this.opt=e)}}init(){if(e.cM("init"),void 0===this.opt)throw new Error("opt not set, required by GAM Loader");e.cM("init brand survey service"),this.getUserMetaPromise=this.getUserMeta(),e.cM("setup message handler"),window.addEventListener("message",e=>{this.onmessage(e)})}handleSlotRenderedNoAdReport(){if(googletag.pubads().addEventListener("slotRenderEnded",e=>this.applyExtraMarginBottom(e)),Array.isArray(this.slotsRenderedEvents))for(var e=0;e<this.slotsRenderedEvents.length;e++)this.applyExtraMarginBottom(this.slotsRenderedEvents[e])}onmessage(t){let s="omni";if(t.data&&("string"==typeof t.data||t.data instanceof String))if(0===t.data.indexOf("get-omni-")){e.cM("Recevied get-omni message, sending back omni");var n=t.source,a=this.opt.omni,i="string"==typeof a?a:"";n.postMessage([s,i,this.opt.perRequestGuid].join("|"),"*")}else if(0===t.data.indexOf("collapse-")){e.cM("Recevied collapse message, collapse ad iframe"),e.cM(t);for(var r=t.source.window,d=document.getElementsByTagName("IFRAME"),l=0;l<d.length;l++){var g=d[l];if(g.contentWindow==r)return void(0,o.wo)(g.parentElement.parentElement.parentElement)}}else if(0===t.data.indexOf("resize|")){e.cM("Recevied resize message, resize ad iframe"),e.cM(t);let s=this._getFrameByEvent(t),n=t.data.indexOf("|")+1,o=t.data.slice(n),a=parseFloat(o)+.5;e.cM("New iframe height "+a),s.height=a.toString(),s.parentElement.style.height=a.toString()+"px"}else if(0===t.data.indexOf("getmarkup|")){let s=t.data.indexOf("|")+1,n=t.data.slice(s);e.cM("Recevied get markup message: "+n);let o=this._getFrameByEvent(t).closest(".everyonelovesstackoverflow");const a=document.createElement("script");a.dataset.adZoneId=o.id,a.src=n,document.body.appendChild(a)}else if(0===t.data.indexOf("window-location|")){let s=t.data.indexOf("|")+1,n=t.data.slice(s);e.cM("Recevied window location message: "+n),n.startsWith("/")||(n="/"+n),window.open(window.location.protocol+"//"+window.location.host+n,"_blank")}else if(0===t.data.indexOf("request-brand-survey-submit|")){let s=t.data.split("|"),n=s[1],o=s[2],a=s[3],i=JSON.parse(a);e.cM(n),e.cM(o),e.cM(a),e.cM("Received brand survey "+n+" response message: "+o);var _=new FormData;for(var b in i)_.append(b,i[b]);let r=this._getFrameByEvent(t);if(v.alreadyCompletedThisBrandSurvey(+n))return e.cM("Already completed this brand survey.  Not submitting duplicate to server."),void r.contentWindow.postMessage("response-brand-survey-submit-duplicate|","*");e.cM("Send the brand survey to the server"),fetch(o,{method:"POST",body:_}).then(e=>e.json()).then(e=>r.contentWindow.postMessage({messageType:p},"*")).catch(e=>r.contentWindow.postMessage({messageType:p},"*"))}else if(0===t.data.indexOf("brand-survey-completed-store|")){let s=t.data.split("|"),n=(s[1],s[2]);if(e.cM("Received brand survey completed store message for survey ID "+n),v.alreadyCompletedThisBrandSurvey(+n))return void e.cM("Already completed this brand survey.  Not recording duplicate locally.");e.cM("Record brand survey completion locally"),(new c).recordBrandSurveyCompleted(+n)}else if(0===t.data.indexOf(h)){let s=t.data.split("|"),n=s[1],o=s[2];e.cM("Received message: "+h+" with Brand Survey ID "+o);let a=(new c).getBrandSurveyEngagement().getBrandLineItemImpressions(+n),i=JSON.stringify(a),r=this._getFrameByEvent(t);e.cM("sending impression data: "+i),r.contentWindow.postMessage("response-brand-survey-metadata|"+this.opt.responseHash+"|"+this.opt.perRequestGuid+"|"+i+"|"+this.opt.countryCode+"|"+this.opt.qualtricsSurveyData,"*")}else if(0===t.data.indexOf("refresh-if-duplicate-brand-survey|")){let e=t.data.split("|")[1],s=this.getSlotElementIdByEvent(t);v.refreshAdIfBrandSurveyIsDuplicated(googletag,+e,s)}else if(0===t.data.indexOf(m)){e.cM("Received message: "+m+" with args: "+t.data);let s=t.data.split("|"),n=s[1],o=s[2],a=s[3],i=s[4],r=new FormData;r.append("brandSurveyId",a.toString()),r.append("responseHash",this.opt.responseHash),r.append("perRequestGuid",this.opt.perRequestGuid),r.append("questionNumber",n.toString()),r.append("metricType",i.toString()),fetch(o,{method:"POST",body:r}).then(e=>e.ok).catch(t=>{e.cM("SendMetricToServer: Error sending metric to server: "+t)})}else if(0===t.data.indexOf(u)){e.cM("Received message: "+u+" with args: "+t.data);let s=this._getFrameByEvent(t);if(!this.opt.targeting["so-tag"])return void s.contentWindow.postMessage(f,"*");const n=this.opt.targeting["so-tag"].join(",");e.cM("sending targeting tags: "+n),s.contentWindow.postMessage(f+n,"*")}else e.cM("Received unhandled message")}getSlotElementIdByEvent(e){let t=this._getFrameByEvent(e),s=t.parentElement?.parentElement?.id;return s||""}_getFrameByEvent(e){return Array.from(document.getElementsByTagName("iframe")).filter(t=>t.contentWindow===e.source)[0]}classifyZoneIds(e){const t=e.map(o.Nj).filter(o.yb);return{eligible:t.filter(o.xb).filter(o.pn),ineligible:t.filter(o.xj)}}applyExtraMarginBottom(t){if(t&&t.slot&&!t.isEmpty&&(t.creativeId||t.lineItemId||!t.isEmpty)){var s=t.slot.getSlotElementId();if(s){var o=document.getElementById(s);if(o)if((0,n.eq)(s)){var a=o?.closest(".js-zone-container");a.style.marginBottom="24px",e.cM("Applied extra margin to the bottom of "+s)}else e.cM("Not applying extra margin to the bottom of "+s+": shouldHaveReportButton = false");else e.cM("Not applying extra margin to the bottom of "+s+": resolved invalid adUnit element")}else e.cM("Not applying extra margin to the bottom of element: invalid adUnitElementId")}else e.cM("Not applying extra margin to the bottom of element: invalid SlotRenderEndedEvent")}async load(s=(0,n.kG)()){const r=this.opt.tlb_position===t.Above?["dfp-mlb","dfp-smlb"]:["dfp-mlb","dfp-smlb","dfp-tlb"];if(!this.isGptReady())return e.cM("Initializing..."),this.initGpt(),void googletag.cmd.push(()=>this.load(s));this.opt.adReportEnabled?(e.cM("Ad reporting enabled"),this.adReports=new a.t(googletag,this)):(e.cM("Ad reporting not enabled"),this.handleSlotRenderedNoAdReport()),this.opt.refresh?(e.cM("Ad refresh enabled"),this.adRefresh=new i(googletag,this.opt.refreshInterval)):e.cM("Ad refresh not enabled"),this.opt.brandSurveyEnabled&&(e.cM("Brand Survey enabled"),this.brandSurvey=new g(googletag,this.opt.brandSurveySettings)),e.cM("Attempting to load ads into ids: ",s);const{eligible:d,ineligible:l}=this.classifyZoneIds(s);if(this.initDebugPanel(googletag,d.concat(l)),d.forEach(e=>(0,o.cf)(e)),l.forEach(o.wo),0===d.length)return void e.cM("Found no ad ids on page");e.cM("Eligible ids:",d),this.opt.abd&&this.appendAdblockDetector();var c=googletag.pubads().getSlots();if(c){var p=c.filter(e=>s.indexOf(e.getSlotElementId())>=0);googletag.destroySlots(p)}this.opt.sf&&(googletag.pubads().setForceSafeFrame(!0),googletag.pubads().setSafeFrameConfig({allowOverlayExpansion:!0,allowPushExpansion:!0,sandbox:!0})),e.cM("Targeting consent: Checking...");let h=!1,m=!1;void 0!==this.opt.targeting_consent&&(m=!0,e.cM("Targeting consent: Parameter set"),e.cM("Targeting consent: Consent given? ",this.opt.targeting_consent),h=this.opt.targeting_consent),void 0!==this.opt.personalization_consent&&(e.cM("Personalization consent: Parameter set"),e.cM("Personalization consent: Consent given? ",this.opt.personalization_consent),h=h&&this.opt.personalization_consent),h=h&&m,this.setPrivacySettings(h),this.opt.ll||googletag.pubads().enableSingleRequest(),cam.sreEvent||(googletag.pubads().addEventListener("slotRenderEnded",e=>this.onSlotRendered(e)),cam.sreEvent=!0),await this.setTargeting();var u=d.filter(e=>!this.opt.ll||r.indexOf(e.id)<0),f=d.filter(e=>!!this.opt.ll&&r.indexOf(e.id)>=0);e.cM("Up front ids:",u),e.cM("Lazy loaded ids:",f),u.forEach(t=>{e.cM(`Defining ad for element ${t.id}`),this.defineSlot(t.id,googletag),t.setAttribute("data-dfp-zone","true")}),googletag.enableServices(),u.forEach(t=>{e.cM(`Displaying ad for element ${t.id}`),this.clc_options.dv_enabled?window.onDvtagReady(function(){googletag.display(t.id)}):googletag.cmd.push(()=>googletag.display(t.id))}),this.opt.ll&&(e.cM("Enabling lazy loading for GAM"),googletag.pubads().enableLazyLoad({fetchMarginPercent:0,renderMarginPercent:0}),e.cM("Setting up lazy loaded ad units"),f.forEach(t=>{e.cM(`Lazy loading - Defining Slot ${t.id}`),this.defineSlot(t.id,googletag)}),f.forEach(t=>{e.cM(`Lazy loading - Displaying ad for element ${t.id}`),this.clc_options.dv_enabled?window.onDvtagReady(function(){googletag.display(t.id)}):googletag.cmd.push(()=>googletag.display(t.id))}))}setPrivacySettings(e){e||googletag.pubads().setPrivacySettings({nonPersonalizedAds:!0})}async setTargeting(){if(!googletag)throw new Error("googletag not defined");let t=this.opt.targeting;if(!t)throw new Error("Targeting not defined (is "+typeof t+")");Object.keys(t).forEach(s=>{e.cM(`-> targeting - ${s}: ${t[s]}`),googletag.pubads().setTargeting(s,t[s])});let s=!1;if(void 0!==this.opt.targeting_consent&&(s=this.opt.targeting_consent),s){let t=(new c).getBrandSurveyEngagement();if(t.getTotalBrandImpressions().forEach((t,s)=>{e.cM(`-> targeting - BrandImpressions: ${s}: ${t}`),googletag.pubads().setTargeting("brand_"+s.toString()+"_impressions",t.toString())}),t.surveysIdsCompleted.forEach(t=>{e.cM(`-> targeting - SurveysTaken: ${t}`),googletag.pubads().setTargeting("survey_"+t+"_taken","true")}),this.clc_options.tgt_e&&this.getUserMetaPromise){let t=await this.getUserMetaPromise;t&&t.tgt_acct?(e.cM("-> targeting - User Account: "+t.tgt_acct),googletag.pubads().setTargeting("user-acct",t.tgt_acct.company_name),googletag.pubads().setTargeting("user_acct_top",t.tgt_acct.company_name),googletag.pubads().setTargeting("user_industry",t.tgt_acct.industry),googletag.pubads().setTargeting("user_employee_count",t.tgt_acct.employee_range)):e.cM("-> targeting - User Account: Not Found"),t&&Object.prototype.hasOwnProperty.call(t,"is_high_rep_earner")?(e.cM("-> targeting - High Rep Earner: "+t.is_high_rep_earner),googletag.pubads().setTargeting("IsHighRepEarner",t.is_high_rep_earner?"true":"false")):e.cM("-> targeting - High Rep Earner: not found")}if(localStorage){e.cM('Checking local storage for "jobs-last-clicked" key.');let t=localStorage.getItem("jobs-last-clicked")?"true":"false";e.cM(`-> targeting - jobs_clicked: ${t}`),googletag.pubads().setTargeting("jobs_clicked",t)}}}appendAdblockDetector(){const e=document.createElement("div");e.className="adsbox",e.id="clc-abd",e.style.position="absolute",e.style.pointerEvents="none",e.innerHTML="&nbsp;",document.body.appendChild(e)}onSlotRendered(s){try{const i=s.slot.getSlotElementId();let r=[];i||r.push("id=0");const d=document.getElementById(i);if(i&&!d&&r.push("el=0"),0!==r.length)return void this.stalled(r.join("&"));const{path:l,sizes:c,zone:g}=(0,n.Z7)(i);if(this.collapsed[g]&&s.isEmpty)return e.cM(`No line item for the element #${d.id}... collapsing.`),void(0,o.wo)(d);if(this.slotsRenderedEvents.push(s),s.lineItemId||s.creativeId||!s.isEmpty){e.cM(`Rendered ad for element #${d.id} [line item #${s.lineItemId}]`),e.cM(s);var a=d.parentElement;if(a.classList.contains("js-zone-container")){switch((0,o.cf)(a),i){case"dfp-tlb":this.opt.tlb_position===t.Above?a.classList.add("mb8"):a.classList.add("mt16");break;case"dfp-tag":a.classList.add("mb8");break;case"dfp-msb":a.classList.add("mt16");break;case"dfp-mlb":case"dfp-smlb":case"dfp-bmlb":a.classList.add("my8");break;case"dfp-isb":a.classList.add("mt24");break;case"dfp-m-aq":a.classList.add("my12"),a.classList.add("mx-auto")}(0,o.$Z)(a),(0,o.$Z)(d)}else e.cM(`No ad for element #${d.id}, collapsing`),e.cM(s),(0,o.wo)(d)}}catch(t){e.cM("Exception thrown onSlotRendered"),e.cM(t),this.stalled("e=1")}}stalled(e){(new Image).src=`https://${this.clc_options.h}/stalled.gif?${e}`}defineSlot(t,s){"dfp-isb"===t&&(e.cM("-> targeting - Sidebar: Inline"),s.pubads().setTargeting("Sidebar",["Inline"])),"dfp-tsb"===t&&(e.cM("-> targeting - Sidebar: Right"),s.pubads().setTargeting("Sidebar",["Right"]));const{path:o,sizes:a,zone:i}=(0,n.Z7)(t);e.cM(`Defining slot for ${t}: ${o}, sizes: ${JSON.stringify(a)}`),s.defineSlot(o,a,t).addService(s.pubads())}importGptLibrary(){this.gptImported||(this.gptImported=!0,void 0===this.opt.targeting_consent||this.opt.targeting_consent?(0,o.Gx)("https://securepubads.g.doubleclick.net/tag/js/gpt.js"):(0,o.Gx)("https://pagead2.googlesyndication.com/tag/js/gpt.js"))}importDvLibrary(){this.clc_options.dv_enabled&&(e.cM("Adding DoubleVerify library"),(0,o.Gx)("https://pub.doubleverify.com/dvtag/21569774/DV1289064/pub.js"),e.cM("Adding DoubleVerify onDvtagReady handler"),window.onDvtagReady=function(t,s=750){e.cM("DoubleVerify onDvtagReady called"),window.dvtag=window.dvtag||{},dvtag.cmd=dvtag.cmd||[];const n={callback:t,timeout:s,timestamp:(new Date).getTime()};dvtag.cmd.push(function(){dvtag.queueAdRequest(n)}),setTimeout(function(){const e=n.callback;n.callback=null,e&&e()},s)})}isGptReady(){return"undefined"!=typeof googletag&&!!googletag.apiReady}initGpt(){"undefined"==typeof googletag&&(window.googletag={cmd:(0,o.QZ)(()=>{this.importGptLibrary(),this.importDvLibrary()})})}getUserMeta(){if(this.opt.allowAccountTargetingForThisRequest&&this.clc_options.tgt_e&&this.clc_options.tgt_p>0){if(e.cM("Targeting enabled."),this.clc_options.tgt_p<100){e.cM("Targeting rate limit enabled.  Rolling the dice...");const t=Math.floor(100*Math.random())+1;if(e.cM("Rolled "+t+" and the max is "+this.clc_options.tgt_p),t>this.clc_options.tgt_p)return void e.cM("Will not request targeting.")}return e.cM("Will request targeting."),function(e,t,s,n){if(t){const t=new Headers;return t.append("Accept","application/json"),async function(e,t={},s=5e3){if("number"!=typeof s&&null!=s&&!1!==s){if("string"!=typeof s)throw new Error("fetchWithTimeout: timeout must be a number");if(s=parseInt(s),isNaN(s))throw new Error("fetchWithTimeout: timeout must be a number (or string that can be parsed to a number)")}const n=new AbortController,{signal:o}=n,a=fetch(e,{...t,signal:o}),i=setTimeout(()=>n.abort(),s);try{const e=await a;return clearTimeout(i),e}catch(e){throw clearTimeout(i),e}}(s+"?"+new URLSearchParams({omni:e}),{method:"GET",mode:"cors",headers:t},n).then(e=>e.json())}return Promise.reject("No consent")}(this.opt.omni,this.opt.targeting_consent,this.clc_options.tgt_u,this.clc_options.tgt_to).catch(t=>{e.vU("Error fetching user account targeting"),e.vU(t)})}e.cM("Targeting disabled.  Will not request account targeting data.")}initDebugPanel(t,s){e.cM("initDebugPanel"),e.cM("Not showing debug panel.")}},window.clcGamLoaderOptions&&(cam.init(),cam.load())})()})();</script>
        
    <footer id="footer" class="site-footer js-footer theme-light__forced" role="contentinfo">
        <div class="site-footer--container">
                <div class="site-footer--logo">

                    <a href="https://stackoverflow.com" aria-label="Stack Overflow"><svg aria-hidden="true" class="native svg-icon iconGlyphMd" width="32" height="37"  viewBox="0 0 32 37"><path fill="#BCBBBB" d="M26 33v-9h4v13H0V24h4v9z"/><path fill="#F48024" d="m21.5 0-2.7 2 9.9 13.3 2.7-2zM26 18.4 13.3 7.8l2.1-2.5 12.7 10.6zM9.1 15.2l15 7 1.4-3-15-7zm14 10.79.68-2.95-16.1-3.35L7 23zM23 30H7v-3h16z"/></svg></a>
                </div>
            <nav class="site-footer--nav" aria-label="Footer">
                    <div class="site-footer--col">
                        <h5 class="-title"><a href="https://stackoverflow.com" class="js-gps-track" data-gps-track="footer.click({ location: 2, link: 15})">Stack Overflow</a></h5>
                        <ul class="-list js-primary-footer-links">
                            <li><a href="/questions" class="js-gps-track -link" data-gps-track="footer.click({ location: 2, link: 16})">Questions</a></li>
                                <li><a href="/help" class="js-gps-track -link" data-gps-track="footer.click({ location: 2, link: 3 })">Help</a></li>
                                <li><a class="js-gps-track -link" data-gps-track="footer.click({ location: 2, link: 5 })" href="https://chat.stackoverflow.com/?tab=site&host=stackoverflow.com">Chat</a></li>
                        </ul>
                    </div>
                    <div class="site-footer--col">
                        <h5 class="-title"><a href="https://stackoverflow.co/" class="js-gps-track" data-gps-track="footer.click({ location: 2, link: 19 })">Products</a></h5>
                        <ul class="-list">
                            <li><a href="https://stackoverflow.co/teams/?utm_medium=referral&utm_source=stackoverflow-community&utm_campaign=footer&utm_content=teams" class="js-gps-track -link"
                                                 data-ga="[&quot;teams traffic&quot;,&quot;footer - site nav&quot;,&quot;stackoverflow.com/teams&quot;,null,{&quot;dimension4&quot;:&quot;teams&quot;}]"
                                                 data-gps-track="footer.click({ location: 2, link: 29 })">Teams</a></li>
                            <li><a href="https://stackoverflow.co/advertising/?utm_medium=referral&utm_source=stackoverflow-community&utm_campaign=footer&utm_content=advertising" class="js-gps-track -link" data-gps-track="footer.click({ location: 2, link: 21 })">Advertising</a></li>
                            <li><a href="https://stackoverflow.co/advertising/employer-branding/?utm_medium=referral&utm_source=stackoverflow-community&utm_campaign=footer&utm_content=talent" class="js-gps-track -link" data-gps-track="footer.click({ location: 2, link: 20 })">Talent</a></li>
                        </ul>
                    </div>
                <div class="site-footer--col">
                    <h5 class="-title"><a class="js-gps-track" data-gps-track="footer.click({ location: 2, link: 1 })" href="https://stackoverflow.co/">Company</a></h5>
                    <ul class="-list">
                            <li><a class="js-gps-track -link" data-gps-track="footer.click({ location: 2, link: 1 })" href="https://stackoverflow.co/">About</a></li>
                        <li><a class="js-gps-track -link" data-gps-track="footer.click({ location: 2, link: 27 })" href="https://stackoverflow.co/company/press/">Press</a></li>
                            <li><a class="js-gps-track -link" data-gps-track="footer.click({ location: 2, link: 9 })" href="https://stackoverflow.co/company/work-here/">Work Here</a></li>
                        <li><a class="js-gps-track -link" data-gps-track="footer.click({ location: 2, link: 7 })" href="https://stackoverflow.com/legal">Legal</a></li>
                        <li><a class="js-gps-track -link" data-gps-track="footer.click({ location: 2, link: 8 })" href="https://stackoverflow.com/legal/privacy-policy">Privacy Policy</a></li>
                        <li><a class="js-gps-track -link" data-gps-track="footer.click({ location: 2, link: 37 })" href="https://stackoverflow.com/legal/terms-of-service/public">Terms of Service</a></li>
                            <li><a class="js-gps-track -link" data-gps-track="footer.click({ location: 2, link: 13 })" href="/contact">Contact Us</a></li>
                            <li id="consent-footer-link"><button type="button" data-controller="cookie-settings" data-action="click->cookie-settings#toggle" class="s-btn s-btn__link py4 js-gps-track -link" data-gps-track="footer.click({ location: 2, link: 38 })" data-consent-popup-loader="footer">Cookie Settings</button></li>
                        <li><a class="js-gps-track -link" data-gps-track="footer.click({ location: 2, link: 39 })" href="https://stackoverflow.com/legal/cookie-policy">Cookie Policy</a></li>
                    </ul>
                </div>
                <div class="site-footer--col site-footer--categories-nav">
                    <div>
                        <h5 class="-title"><a href="https://stackexchange.com" data-gps-track="footer.click({ location: 2, link: 30 })">Stack Exchange Network</a></h5>
                        <ul class="-list">
                            <li>
                                <a href="https://stackexchange.com/sites#technology" class="-link js-gps-track" data-gps-track="footer.click({ location: 2, link: 24 })">
                                    Technology
                                </a>
                            </li>
                            <li>
                                <a href="https://stackexchange.com/sites#culturerecreation" class="-link js-gps-track" data-gps-track="footer.click({ location: 2, link: 24 })">
                                    Culture &amp; recreation
                                </a>
                            </li>
                            <li>
                                <a href="https://stackexchange.com/sites#lifearts" class="-link js-gps-track" data-gps-track="footer.click({ location: 2, link: 24 })">
                                    Life &amp; arts
                                </a>
                            </li>
                            <li>
                                <a href="https://stackexchange.com/sites#science" class="-link js-gps-track" data-gps-track="footer.click({ location: 2, link: 24 })">
                                    Science
                                </a>
                            </li>
                            <li>
                                <a href="https://stackexchange.com/sites#professional" class="-link js-gps-track" data-gps-track="footer.click({ location: 2, link: 24 })">
                                    Professional
                                </a>
                            </li>
                            <li>
                                <a href="https://stackexchange.com/sites#business" class="-link js-gps-track" data-gps-track="footer.click({ location: 2, link: 24 })">
                                    Business
                                </a>
                            </li>

                            <li class="mt16 md:mt0">
                                <a href="https://api.stackexchange.com/" class="-link js-gps-track" data-gps-track="footer.click({ location: 2, link: 24 })">
                                    API
                                </a>
                            </li>

                            <li>
                                <a href="https://data.stackexchange.com/" class="-link js-gps-track" data-gps-track="footer.click({ location: 2, link: 24 })">
                                    Data
                                </a>
                            </li>
                        </ul>
                    </div>
                </div>
            </nav>
            <div class="site-footer--copyright fs-fine md:mt24">
                <ul class="-list -social md:mb8">
                    <li><a class="js-gps-track -link" data-gps-track="footer.click({ location: 2, link:4 })" href="https://stackoverflow.blog?blb=1">Blog</a></li>
                    <li><a href="https://www.facebook.com/officialstackoverflow/" class="-link js-gps-track" data-gps-track="footer.click({ location: 2, link: 31 })">Facebook</a></li>
                    <li><a href="https://twitter.com/stackoverflow" class="-link js-gps-track" data-gps-track="footer.click({ location: 2, link: 32 })">Twitter</a></li>
                    <li><a href="https://linkedin.com/company/stack-overflow" class="-link js-gps-track" data-gps-track="footer.click({ location: 2, link: 33 })">LinkedIn</a></li>
                    <li><a href="https://www.instagram.com/thestackoverflow" class="-link js-gps-track" data-gps-track="footer.click({ location: 2, link: 36 })">Instagram</a></li>
                </ul>

                <p class="md:mb0">
                    <span>Site design / logo © 2024 Stack Exchange Inc; </span>
                    <span>user contributions licensed under </span>
                    <a class="-link s-link td-underline" href="https://stackoverflow.com/help/licensing">CC BY-SA</a>
                    <span>. </span>
                    <span id="svnrev">rev&nbsp;2024.12.18.20664</span>
                </p>
            </div>
        </div>

    </footer>


    

            <!-- Google tag (gtag.js) -->
            <script async src="https://www.googletagmanager.com/gtag/js?id=G-WCZ03SZFCQ"></script>
            <script>
                window.dataLayer = window.dataLayer || [];
                function gtag() { dataLayer.push(arguments); }
            </script>
            <script>
                (function(i, s, o, g, r, a, m) {
                    i['GoogleAnalyticsObject'] = r; i[r] = i[r] || function() { (i[r].q = i[r].q || []).push(arguments) }, i[r].l = 1 * new Date(); a = s.createElement(o),
                        m = s.getElementsByTagName(o)[0]; a.async = 1; a.src = g; m.parentNode.insertBefore(a, m);
                })(window, document, 'script', 'https://www.google-analytics.com/analytics.js', 'ga');
            </script>
        <script>
            StackExchange.ready(function() {

                var ga3Settings = {
                    autoLink: ["stackoverflow.blog","info.stackoverflowsolutions.com","stackoverflowsolutions.com"],
                    sendTitles: true,
                    tracker: window.ga,
                    trackingCodes: [
                        'UA-108242619-1'
                    ],
                    checkDimension: 'dimension42'
                };

                var customGA4Dimensions = {};


                customGA4Dimensions["requestid"] = "7622944e-81f5-4ffb-a866-9de0381416ff";

                    customGA4Dimensions["routename"] = "Questions/Show";

                    customGA4Dimensions["sub_communities"] = "mobile-dev";

                    customGA4Dimensions["post_id"] = "35302978";


                    customGA4Dimensions["tags"] = "|android|android-sensors|sensormanager|android-developer-api|proximitysensor|";


                var ga4Settings = {
                    tracker: gtag,
                    trackingCodes: [
                        'G-WCZ03SZFCQ'
                    ],
                    consentsToPerformanceCookies: "granted",
                    consentsToTargetingCookies: "granted",
                    eventParameters: customGA4Dimensions,
                    checkForAdBlock: true,
                    sendTitles: true,
                    trackClicks: false,
                };

                StackExchange.ga.init({ GA3: ga3Settings, GA4: ga4Settings });


                StackExchange.ga.setDimension('dimension2', '|android|android-sensors|sensormanager|android-developer-api|proximitysensor|');

                StackExchange.ga.setDimension('dimension43', 'mobile-dev');

                StackExchange.ga.setDimension('dimension3', 'Questions/Show');


                StackExchange.ga.setDimension('dimension7', "1734583726.1648995979");

                StackExchange.ga.trackPageView();
            });
        </script>
        
            <script src="https://cdn.cookielaw.org/scripttemplates/otSDKStub.js" charset="UTF-8" data-document-language="true" data-domain-script="c3d9f1e3-55f3-4eba-b268-46cee4c6789c"></script>
<script defer src="https://cdn.sstatic.net/Js/modules/cookie-consent.en.js?v=36bebc18e04f"></script>

    
    <script>(function(){function c(){var b=a.contentDocument||a.contentWindow.document;if(b){var d=b.createElement('script');d.innerHTML="window.__CF$cv$params={r:'8f44c320bbe62113',t:'MTczNDU4MzcyNi4wMDAwMDA='};var a=document.createElement('script');a.nonce='';a.src='/cdn-cgi/challenge-platform/scripts/jsd/main.js';document.getElementsByTagName('head')[0].appendChild(a);";b.getElementsByTagName('head')[0].appendChild(d)}}if(document.body){var a=document.createElement('iframe');a.height=1;a.width=1;a.style.position='absolute';a.style.top=0;a.style.left=0;a.style.border='none';a.style.visibility='hidden';document.body.appendChild(a);if('loading'!==document.readyState)c();else if(window.addEventListener)document.addEventListener('DOMContentLoaded',c);else{var e=document.onreadystatechange||function(){};document.onreadystatechange=function(b){e(b);'loading'!==document.readyState&&(document.onreadystatechange=e,c())}}}})();</script></body>
    </html>
"""
base_url = "https://stackoverflow.com/questions/35302978/how-to-get-current-value-of-androids-proximity-sensor"
