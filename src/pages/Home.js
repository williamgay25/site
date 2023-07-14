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
          <h2>previously</h2>
          <ul>
            <li>industrial engineer @ <a href="https://www.gatech.edu">georgia tech</a> - a lot of statistics and data modeling.</li>
            <li>summer analyst @ <a href="https://homrichberg.com">homrich berg</a> - first employee to download python on a work computer.</li>
            <li>investment banking summer analyst @ <a href="https://www.croft-bender.com">croft &amp; bender</a> - wrote python and vba to automate most of my work.</li>
          </ul>
        </section>

        <section>
          <h2>wannabe founder</h2>
          <ul>
            <li><a href="https://tempus-ex.com">tempus ex machina</a> - worked on a fan engagement startup with the nfl. wrote some react native that didn't work.</li>
            <li><a href="https://findflayr.com">flayrai</a> - capstone project turned accelerator. worked on restaurant hiring and learned a lot.</li>
            <li><a href="https://iterate.tools">iterate.tools</a> - building a AI-powered website builder. sign up today!</li>
          </ul>
        </section>

        <section>
          <h2>currently hacking on</h2>
          <ul>
            <li><a href="https://github.com/williamgay25/micrograd">micrograd</a> - building a neural net library from scratch.</li>
            <li><a href="https://github.com/williamgay25/makemore">makemore</a> - working on a character level language model.</li>
            <li><a href="https://github.com/williamgay25/toolbox">toolbox</a> - building a hub for tools i use too often.</li>
            <li><a href="https://github.com/williamgay25/crawler">crawler</a> - basic python web crawler.</li>
          </ul>
        </section>
    </div>
  );
}

export default Home;