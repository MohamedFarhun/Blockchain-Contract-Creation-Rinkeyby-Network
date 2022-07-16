/**
     * @type import('hardhat/config').HardhatUserConfig
     */
 require('dotenv').config(); //all the key value pairs are being made available due to this lib
 require('@nomiclabs/hardhat-ethers');
 let secret =require("./secret")
 const {url,accounts} = process.env; //environment variables are being loaded here.
 module.exports = {
   solidity: "0.7.3",
   defaultNetwork: 'rinkeby',
   networks: {
    rinkeby:{
        url:secret.url,
        accounts:[secret.key],
    }
    
 }
}