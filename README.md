# Laravel Web App template theme free download source code

A landing page website build with laravel the php artisan

Demo : [https://viceconsultingengineering.ro/home)

https://github.com/oceanprotocol/ocean-node
https://github.com/oceanprotocol/ocean.py
https://docs.desights.ai/core-components/registry
https://github.com/oceanprotocol/market
https://github.com/oceanprotocol/waves
https://github.com/oceanprotocol/token-gating-template
https://github.com/oceanprotocol/tokengated-next-chatgpt
https://www.figma.com/proto/8nT6qEUMMmJsMs8Ow2KzAN/OceanLearn?type=design&scaling=min-zoom&page-id=5%3A44&starting-point-node-id=5%3A91&node-id=5-91
https://www.figma.com/proto/xReYRMMnhrynRsNqdy63tT/OceanReads?type=design&node-id=135-92&scaling=min-zoom&page-id=28%3A380&starting-point-node-id=135%3A92
https://www.figma.com/proto/lu5ODNDwIrJmlM0WqBeBJ3/OceanTickets?page-id=75%3A386&type=design&node-id=336-126&viewport=131%2C706%2C0.19&t=ia9UyDUfZxZQS4k1-1&scaling=scale-down&starting-point-node-id=336%3A126
https://www.figma.com/proto/LwbMqloVagXnmlaeDCFiJC/OceanArt?type=design&node-id=13-169&scaling=min-zoom&page-id=13%3A122&starting-point-node-id=13%3A169
https://www.figma.com/proto/xAcyc0rqZNTA8TdW43NN5P/WebPalette?type=design&node-id=9-138&scaling=min-zoom&page-id=0%3A1&starting-point-node-id=9%3A138
https://marketplace.future-mobility-alliance.org


Ocean is proud to release the integration of Compute-to-Data into Ocean Market.
This enables buying & selling of private data, while preserving privacy.
Compute-to-Data resolves the tradeoff between the benefits of using private data, and the risks of exposing it. It does so by providing a means to exchange data while preserving privacy by allowing the data to stay on-premise with data publishers, yet allows data consumers to run compute jobs on data — all through the Ocean Market interface.
Therefore:
Data owners can monetize data while preserving privacy & control;
Yet data buyers can create value from it with analytics jobs, AI modeling, and more.
Data publishers approve algorithms to run on their data and then the Compute-to-Data environment orchestrates remote computation and execution on data while preserving the privacy of the data. The blockchain-based smart contracts ensure that every data publisher / AI practitioner can verify proper execution of their algorithm.
Users can benefit from this technology in a number of ways.
Data owners can monetize their data while maintaining privacy and control.
Data consumers can access private data without liability of directly seeing private data.
AI practitioners & data scientists can access valuable, private data that was previously unavailable, which can lead to more accurate AI models to improve research and business outcomes.
AI practitioners can also publish their own algorithms,allowing them to earn passive income every time their algorithm is downloaded or run as part of a Compute Job. They can even retain privacy of the algorithms themselves.
Businesses and entrepreneurs can quickly launch their own data marketplace for their vertical, and leverage Compute-to-Data to preserve their sellers’ privacy and support more compute & AI flows.
This release makes Ocean Compute-to-Data available to be more widely used via Ocean Market, building on backend support and private enterprise frontend work that goes back almost a year. The learnings from these initial deployments all fed back into this release. We’re very excited to take another big step towards realizing our vision of data as a new asset class.
– Alex Coseru, VP of Engineering at Ocean Protocol
This launch is a major milestone in our 2021 Product Roadmap. It greatly enhances privacy protection and breadth of applicability in Ocean Market and other Ocean-powered marketplaces..
We’re excited to give our first Compute-to-Data implementation in Ocean Market into the hands of our community. We invite you to try out, to explore, to stress-test, and to give us feedback, because the beauty of open-source is that our code and work process is public for all to see and utilize. And with key Compute-to-Data user flows now directly integrated into Ocean Market, developers can use the code as a boilerplate for their own flows or integrations.
– Matthias Kretschmann, Designer & Developer on Ocean Market
Data Sets & Algorithms
With Compute-to-Data, data sets are not allowed to leave the premises of the data holder, and with that we’re introducing a new asset type: algorithms.

Visual distinction between a public algorithm and a compute data set.
Algorithms are small (or complex) scripts that are allowed to run on data sets under certain conditions within an isolated and secure environment. They can be either public or private, and just like data sets, they can have a pool or a fixed price to determine their price whenever they are used. An algorithm set to public can be downloaded for its set price, while an algorithm set to private is only available as part of a compute job without any way to download it.
For each data set, publishers can select the specific algorithms they permit on their data set, or simply allow all published algorithms. The implementation in Ocean Market is private by default: upon publishing a compute data set, no algorithms are allowed to run on it. This is to prevent data escape by a rogue algorithm being written in a way to extract all data from a data set. This is why the most public option of allowing all published algorithms should be handled with care too.
Check it out
Everything is live in Ocean Market right now, in all supported networks: Ethereum Mainnet, Polygon/Matic, Rinkeby, and Ropsten.

A compute data set with allowed algorithm on Polygon/Matic: market.oceanprotocol.com/asset/did:op:76E031A63e4dAB370Ae25b1A93A997e79e084f6f
We suggest checking out the Ocean Market connected to Polygon/Matic where you can already find some compute data sets and algorithms, and you will enjoy fast and cheap transactions. Switch your wallet to Polygon/Matic, or use the chain preference:

We’ve also prepared a walkthrough of the key user flows in Ocean Market recorded during the first tech demo:

Video walkthrough of the key user flows in Ocean Market.
Publish a Compute Data Set
When publishing a data set, you’ll see a new option under Access Type. You can now choose Compute to make data sets available for Compute-to-Data (but not for download, for example).

Data Publisher Flow: Set Access Type for your data set to Compute or Download.
When inspecting a compute data set after publishing, you’ll see a new Edit Compute Settings button.

Data Publisher Flow: New asset action for compute settings.
This button brings you to a screen where you can choose which algorithms you want to allow on the data set.

Data Publisher Flow: Define algorithms allowed to run on your data set.
Publish an Algorithm
To publish an algorithm, you simply host a script file and point to its URL, just as with data sets. Then you define the Docker environment you want your script to run under.
See this tutorial with examples for the specifics of how an algorithm needs to be authored.

Algorithm Publisher Flow.
After publishing, you set either a fixed or dynamic price, just like on data sets.
Start a Compute Job
Go to the data set you’d like to analyze. Under the Use tab, you can choose from a drop-down list of allowed algorithms which ones you’d like to run on the data set. Choose the algorithm, then click Buy Compute Job. This buys you (compute) access to both items: to the data set (for the duration that the data publisher has set) as well as the algorithm.

Starting a Compute Job.
Compute Job Details and Results
Once you start the Compute Job, you’ll see in your history that it’s running. The final output results will be available there, along with further details.

Compute Job details are displayed under History.
Further Technical Resources
Read our technical guides to Ocean Compute-to-Data to learn more about what’s going on under the hood.
Compute to Data Technical Overview
Tutorial: Writing Algorithms for Compute to Data
Tutorial: Set Up a Compute-to-Data Environment (for marketplace owners)
GitHub: oceanprotocol/market
About Ocean Protocol
Ocean Protocol’s mission is to kickstart a Web3 Data Economy that reaches the world, giving power back to data owners and enabling people to capture value from data to better our world.
Data is a new asset class; Ocean Protocol unlocks its value. Data owners and consumers use the Ocean Market app to publish, discover, and consume data assets in a secure, privacy-preserving fashion.
Ocean datatokens turn data into data assets. This enables data wallets, data exchanges, and data co-ops by leveraging crypto wallets, exchanges, and other DeFi tools. Projects use Ocean libraries and OCEAN in their own apps to help drive the Web3 Data Economy.
The Ocean token is used to stake on data, to govern Ocean Protocol’s community funding, and to buy & sell data. Its supply is disbursed over time to drive near-term growth and long-term sustainability. OCEAN is designed to increase with a rise in usage volume.

https://app.lunor.quest/challenge/1000033?utm_source=cto&utm_medium=cto&utm_campaign=cto
![Screenshot 2025-03-09 at 05 04 00](https://github.com/user-attachments/assets/ecca9a11-ae89-4646-b774-acf051986519)
