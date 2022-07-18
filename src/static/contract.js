//Token Trees on ETH:0xfc31a6644059d6b56469b340b74b838397d480d7
//trees_final.sol :
//dweb:/ipfs/QmPLe27poDJ5WtrLFzkfsekoSHP98TfiHG418Ny9i3TqrB
//metadata.json :
//dweb:/ipfs/QmNvwMMKxv2yRbXXF7tEFJEApHHBDgt5K7NWfNGgH7cxtJ
const forwarderOrigin = 'http://localhost:8000'
const initialize = () => {
  const serverUrl = "https://uo5z2mugswff.usemoralis.com:2053/server";
  const appId = "tyX58ChRjFa22ecfFWA9Z4mWOsUF2WKIX7i5hBWB";
  Moralis.initialize(serverUrl); // Application id from moralis.io
  Moralis.serverURL = appId; //Server url from moralis.io
  const contractAddress = "0xfc31a6644059d6b56469b340b74b838397d480d7";
  //Basic Actions Section
  const onboardButton = document.getElementById('connectButton');
  const mintButton = document.querySelector("#mint-btn");
  const copyright = document.querySelector(".copyright")
  copyright.innerText = "© " + new Date().getFullYear() + " TokenTreesNFT.com"
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

function isUserConnected() {
    return user ? true : false;
}

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

  }
   else {
  console.log("already login");
  onboardButton.innerText = "Connected";
  }
}

async function logOut() {
  await Moralis.User.logOut();
  console.log("logged out");
  onboardButton.innerText = "Connect";
}

async function upload(){
mintButton.innerText = "In Progress...";
const mySvg = $("#__turtlegraph__").html();
currentDate = Date.now();
console.log(currentDate);
const treeAddress = document.getElementById("treeAddress").value.slice(0,5);
console.log(mySvg)
//below chunk taken from html script

//script ends
try {
const metadata = {
  "name": `TokenTree - ${treeAddress}`, //needs to be auto updated
  "description": "Generative trees built out of ERC721 tokens in a wallet.",
  "image_data": mySvg,
  "attributes": [
    {
      "trait_type": "Leaves",
      "value": leafColor
      },
      {
      "trait_type": "Roots",
      "value": rootColor
      },
      {
      "trait_type": "Canopy",
      "value": canopy
      },
       {
       "trait_type": "Root Ball",
      "value": rootBall
      },
      {
      "trait_type": "Branch Ramification",
      "value": branchRamification
      },
      {
      "trait_type": "Seeded Block",
      "value": blockNumber.toString()
      },
      {
      "display_type": "date",
      "trait_type": "Seeded On",
      "value": currentDate,
    }
  ]
}
console.log(metadata)
const metadataFile = new Moralis.File("metadata.json", {
  base64: btoa(JSON.stringify(metadata)),
});
await metadataFile.saveIPFS();

const metadataURL = await metadataFile.ipfs();


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
mintButton.innerText = "Mint (0.03 E)";

} catch(err) {
    alert("Generate a tree before minting!");
    console.log(err);
    mintButton.innerText = "Mint (0.03 E)";
}

}

mintButton.onclick = upload;
onboardButton.onclick = login;

console.log(user.get("ethAddress"));

  //------Inserted Code------\\
const MetaMaskClientCheck = () => {
  //Now we check to see if Metmask is installed
  if (!isMetaMaskInstalled()) {
    //If it isn't installed we ask the user to click to install it
    onboardButton.innerText = "Install MetaMask!";
    //When the button is clicked we call th is function
    onboardButton.onclick = onClickInstall;
    //The button is now disabled
    onboardButton.disabled = false;
  } else {
    onboardButton.innerText = 'Connect';
    onboardButton.disabled = false;

  }
};
MetaMaskClientCheck();
login();
//------/Inserted Code------\\
};

window.addEventListener('DOMContentLoaded', initialize)