/*global ethereum, MetamaskOnboarding */

/*
The `piggybankContract` is compiled from:

  pragma solidity ^0.4.0;
  contract PiggyBank {

      uint private balance;
      address public owner;

      function PiggyBank() public {
          owner = msg.sender;
          balance = 0;
      }

      function deposit() public payable returns (uint) {
          balance += msg.value;
          return balance;
      }

      function withdraw(uint withdrawAmount) public returns (uint remainingBal) {
          require(msg.sender == owner);
          balance -= withdrawAmount;

          msg.sender.transfer(withdrawAmount);

          return balance;
      }
  }
*/

const forwarderOrigin = 'http://localhost:8000'
let web3;


const initialize = () => {
  const serverUrl = "https://fzqqgw1gnhcu.usemoralis.com:2053/server";
  const appId = "wZRtpBnfIAxoDmOL9rWnH6a9QCWPxSgpcm6iuFeA";
  Moralis.initialize(serverUrl); // Application id from moralis.io
  Moralis.serverURL = appId; //Server url from moralis.io

  const contractAddress = "0x930061094ec65f7d91199e30DdBd5B0dDdc98Eb6";


  //Basic Actions Section
  const onboardButton = document.getElementById('connectButton');
  const mintButton = document.querySelector("#mint-btn");



  //Created check function to see if the MetaMask extension is installed
  const isMetaMaskInstalled = () => {
    //Have to check the ethereum binding on the window object to see if it's installed
    const { ethereum } = window;
    return Boolean(ethereum && ethereum.isMetaMask);
  };


//const onboarding = new MetaMaskOnboarding({ forwarderOrigin });
Moralis.start({ serverUrl, appId });

let user = Moralis.User.current();
/* Authentication code */
async function login() {

  if (!user) {
    user = await Moralis.authenticate({
      signingMessage: "Log in using Moralis",
    })
      .then(function (user) {
        console.log("logged in user:", user);
        console.log(user.get("ethAddress"));
        onboardButton.innerText = "Connected";
      })
      .catch(function (error) {
        console.log(error);
      });

  } else {
  console.log("already login");
  }
}

async function logOut() {
  await Moralis.User.logOut();
  console.log("logged out");
  onboardButton.innerText = "Connect";
}

async function upload(){
const mySvg = $("#__turtlegraph__").html();
const base64Data = window.btoa(mySvg);
const base64Image = `data:image/svg+xml;base64,${btoa(mySvg)}`;
currentDate = Date.now();
console.log(currentDate);
const treeAddress = document.getElementById("treeAddress").value.slice(0,5);
  console.log(treeAddress);
//const SvgImage = new Moralis.File("image.svg", {base64: base64Image});
//await SvgImage.saveIPFS();
//const imgURL = await SvgImage.ipfs();
//const metadata = {
//  "name": WalletTree, //needs to be auto updated
//  "description": "Unique generative trees built out of ERC721 tokens in your wallet.",
//  "image": imgURL, // received from Moralis IPFS function.
//  "edition": 1, //needs to be auto updated
//  "Block": //block number at creation,
//  "attributes": [
//    {
//      "trait_type": "Leaf Palette",
//      "value": ""}, //To be caught from leaf_palette_name variable in nft_art.py
//      {"trait_type": "Root Palette",
//      "value": ""}, //To be caught from leaf_palette_name variable in nft_art.py
//  ]
//}

const metadata = {
  "name": `WalletTree ${treeAddress}`, //needs to be auto updated
  "description": "Unique generative trees built out of ERC721 tokens in your wallet.",
  "image_data": mySvg, // received from Moralis IPFS function.
  "Block": 000, //block number at creation,
  "attributes": [
    {
      "trait_type": "Leaf Palette",
      "value": ""}, //To be caught from leaf_palette_name variable in nft_art.py
      {"trait_type": "Root Palette",
      "value": ""}, //To be caught from leaf_palette_name variable in nft_art.py
      {
      "display_type": "date",
      "trait_type": "created",
      "value": currentDate,
    }
  ]
}
const metadataFile = new Moralis.File("metadata.json", {
  base64: btoa(JSON.stringify(metadata)),
});
await metadataFile.saveIPFS();
const metadataURL = await metadataFile.ipfs();
//const contract = new web3.eth.Contract(contractAbi, contractAddress)
//contract.methods.mint(metadataURL)
await Moralis.enableWeb3();
const sendOptions = {
  contractAddress: contractAddress,
  functionName: "mint",
  abi: contractAbi,
  msgValue: Moralis.Units.ETH("0.03"),
  params: {
    uri: metadataURL,
  },
};

const transaction = await Moralis.executeFunction(sendOptions);
await transaction.wait()
alert(`Minted Successfully! Txn Hash: ${transaction.hash}`)

}











function onMintClick() {

    console.log(mySvg);
}
mintButton.onclick = upload;
onboardButton.onclick = login;

console.log("useeerrrr"+user);

  //------Inserted Code------\\
const MetaMaskClientCheck = () => {
  //Now we check to see if Metmask is installed
  if (!isMetaMaskInstalled()) {
    //If it isn't installed we ask the user to click to install it
    onboardButton.innerText = 'Click here to install MetaMask!';
    //When the button is clicked we call th is function
    onboardButton.onclick = onClickInstall;
    //The button is now disabled
    onboardButton.disabled = false;
  } else {
    //If MetaMask is installed we ask the user to connect to their wallet
    onboardButton.innerText = 'Connect';
//    //When the button is clicked we call this function to connect the users MetaMask Wallet
//    onboardButton.onclick = await onClickConnect;
//    //The button is now disabled
//    onboardButton.disabled = false;

  }
};
MetaMaskClientCheck();
login();
//------/Inserted Code------\\
};


window.addEventListener('DOMContentLoaded', initialize)