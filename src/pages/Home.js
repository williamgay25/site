import React from 'react';
import Nav from '../components/Nav';

function Home() {
  return (
    <div>
        <header>
            <h1>william gay</h1>
            <Nav />
        </header>

        <section>
          <h2>currently</h2>
          <ul>
            <li>research engineer @ <a href="https://larryheck.github.io/avalab/">ava lab</a> - building ai virtual assistants.</li>
          </ul>
        </section>
        
        <section>
          <h2>previously</h2>
          <ul>
            <li>industrial engineer @ <a href="https://www.gatech.edu">georgia tech</a> - a lot of statistics and data modeling.</li>
            <li>summer analyst @ <a href="https://homrichberg.com">homrich berg</a> - first employee to download python on a work computer.</li>
            <li>investment banking summer analyst @ <a href="https://www.croft-bender.com">croft &amp; bender</a> - wrote python and vba to automate most of my work.</li>
            <li>software engineer @ <a href="https://tempus-ex.com">tempus ex machina</a> - worked on a fan engagement startup with the nfl. wrote some react native.</li>
          </ul>
        </section>

        <section>
          <h2>wannabe founder</h2>
          <ul>
            <li><a href="https://github.com/flayrai">flayrai</a> - capstone project turned startup accelerator. worked on restaurant hiring and learned a lot.</li>
            <li><a href="https://github.com/iteratedottools">iterate.tools</a> - worked on an AI-powered website builder.</li>
          </ul>
        </section>

        <section>
          <h2>freetime projects</h2>
          <ul>
            <li><a href="https://github.com/williamgay25/micrograd">micrograd</a> - building a neural net library from scratch.</li>
            <li><a href="https://github.com/williamgay25/makemore">makemore</a> - working on a character level language model.</li>
            <li><a href="https://github.com/williamgay25/crawler">crawler</a> - basic python web crawler.</li>
          </ul>
        </section>
    </div>
  );
}

export default Home;