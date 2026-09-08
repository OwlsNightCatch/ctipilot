<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8"/>
    <meta name="referrer" content="no-referrer"/>
    <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
    <title>CSH</title>
    <link rel="shortcut icon" type="image/x-icon" href="/img/ico/favicon.ico"/>
    <link rel="icon" type="image/x-icon" href="/img/ico/favicon.ico"/>
    <script src="/assets/ace-builds/ace.js"></script>
    <script src="/assets/theme-loader.js"></script>
    <style>
      .boot {
        position: fixed;
        inset: 0;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        gap: 1.75rem;
        background: #ffffff;
        font-family: -apple-system, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
      }
      .boot__logo {
        width: 180px;
        aspect-ratio: 168.21 / 47.49;
        background: url('/img/logo-CH_light.svg') center / contain no-repeat;
      }
      .boot__spinner {
        display: block;
        width: 2.5rem;
        height: 2.5rem;
        border: 0.25em solid rgba(46, 74, 109, 0.2);
        border-right-color: #2e4a6d;
        border-radius: 50%;
        animation: boot-spin 0.75s linear infinite;
      }
      .dark-mode .boot {
        background: #181919;
      }
      .dark-mode .boot__logo {
        background-image: url('/img/logo-CH_dark.svg');
      }
      .dark-mode .boot__spinner {
        border-color: rgba(99, 148, 209, 0.2);
        border-right-color: #6394d1;
      }
      @keyframes boot-spin {
        to {
          transform: rotate(360deg);
        }
      }
      @media (prefers-reduced-motion: reduce) {
        .boot__spinner {
          animation-duration: 1.5s;
        }
      }
    </style>
  <link rel="stylesheet" href="styles-YAT6HB47.css"></head>
  <body>
    <app-root>
      <div class="boot">
        <div class="boot__logo"></div>
        <output class="boot__spinner" aria-label="Loading"></output>
      </div>
    </app-root>
  <script src="polyfills-RV3JTMEC.js" type="module"></script><script src="scripts-TX3FFEXN.js" defer></script><script src="main-LVMF52LY.js" type="module"></script></body>
</html>
