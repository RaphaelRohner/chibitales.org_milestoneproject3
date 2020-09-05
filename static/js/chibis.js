/*-------------------- FUNCTION FOR ADDITIONAL INFOS NOT AVAILABLE IN APIs --------------------*/
function cardInfos(chibiCard) {    
    
    let result = chibisArray[chibiCard-1];
    
    return result;
}

/*-------------------- GENERATE CARD STATS -------------------- */

function cardInfosHTML(chibiCard, cardTypes) {
    /*----------- Refresh HTML STATUS ----------*/
    $("#chibiCardStatus").html(`Look at this !!`);

    /*----------- Variables for minted cards ----------*/
    let cardAmount;
    let cardBurnt;
    
    /*----------- Catch unminted card and return card numbers ----------*/
    if (chibiCard == 39) {
        cardAmount = 0;
        cardBurnt = 0;
    } else {
        cardAmount = cardTypes[chibiCard].amount;
        cardBurnt = cardTypes[chibiCard].burnt;
    }    

    /*----------- GET CARD STATS FROM CHIBI ARRAY ----------*/
    let arrayLine = cardInfos(chibiCard);

    /*----------- RETURN CARD AND STATS TO HTML ----------*/
    return `
        <div class="col-12 col-sm-6 col-lg-4 col-xl-3 chibi-stats">
            <h4 class="uppercase">${arrayLine.name} - ID ${chibiCard}</h4>
            <p>Source: ${arrayLine.source}</p>
            <p>Existing: ${cardAmount - cardBurnt} ( Created: ${cardAmount} | Burnt: ${cardBurnt} )</p>      
            <img class="img-fluid" src="${"https://chibifighters.s3-us-west-2.amazonaws.com/api/cards/card_" + chibiCard + ".png"}" />            
            <p>Rarity: ${arrayLine.rarity} | Type: ${arrayLine.type} | Slots: ${arrayLine.slots}</p>
            <p>Base-Juice: ${arrayLine.base_juice} | -Health: ${arrayLine.base_health} | -Damage: ${arrayLine.base_dmg}</p>
            <p>Skill: ${arrayLine.skill}</p>
            <p>Charged Skill: ${arrayLine.charged_skill}</p>
        </div>`;       
}

/*-------------------- SEARCH INSTRUCTIONS -------------------- */
function searchInstructions() {
    return `
            <div class="row">
                <div class="col-2">
                    <i class="chibi-infos-icon fa fa-question" aria-hidden="true"></i>
                </div>
                <div class="col-10">
                    <h4 class="chibi-infos-heading uppercase">How to search</h4>
                    <p>Use the fields on the left to either:</p>
                    <ul>                        
                        <li>search by card number</li>
                        <li>search by card name</li>
                        <li>or narrow down with the 4 fields</li>
                    </ul>
                </div>
            </div>`;
}

/*-------------------- CLEAR INPUT FIELDs ON FOCUS -------------------- */
function clearIDSearch(event) {
    document.getElementById('cardNumber').value = "";
}

function clearNameSearch(event) {
    document.getElementById('cardName').value = "";
}

/*-------------------- CREATE CARD BY NUMBER -------------------- */

function findCardByNumber(event) {

    /* ----------- ASSIGN INPUT TO VARIABLE ---------->*/
    let chibiCardNumber = parseInt($("#cardNumber").val());

    /* ----------- CHECK IF INPUT IS IN RANGE -----------> */
    if (chibiCardNumber > 111 || chibiCardNumber < 1) {
        $("#chibiCardImage").html(searchInstructions);
        $("#chibiCardStatus").html(`No such card !!`);
        $("#cardNumber").val("").attr("placeholer", "search by card number").focus();                           
        return;

    /* ----------- CHECK IF INPUT IS A NUMBER -----------> */    
    } else if (isNaN(chibiCardNumber)) {
        $("#chibiCardImage").html(searchInstructions),
        $("#chibiCardStatus").html(`Use a number !!`);
        $("#cardNumber").val("").attr("placeholer", "search by card number").focus();
        return;

    /* ----------- LOADER MESSAGE DURING DELAY -----------> */
    } else {
        $("#chibiCardStatus").html(`<img src="../static/css/loader.gif" alt="loading..." /> Searching !!`);
    }

        // Catch API unavailable --> https://www.denisbouquet.com/stop-ajax-request/                       
    
    /* ----------- LOAD CHIBI API -----------> */
    $.when (        
    $.getJSON(`https://chibifighters.com/api/stats/`)
    ).then(
        function(chibiApiResponse ) {
            let cardTypes = chibiApiResponse.types;
            let chibiCard = chibiCardNumber;
            $("#chibiCardImage").html(cardInfosHTML(chibiCard, cardTypes));     
        },        
        function(errorResponse) {
            if(errorResponse.status === 404) {
                $("#chibiData").html(
                    `<h2>Chibi Fighters down</h2>`);
            } else {
                $("#chibiData").html(
                    `<h2>Error: ${errorResponse.responseJSON.message}</h2>`);            
            }       
        });    
}

/*-------------------- CREATE CARD BY NAME -------------------- */

function findCardByName(event) {

    document.getElementById("cardNameSubmit").addEventListener("click", function(event){
        event.preventDefault();
    });

    /* ----------- ASSIGN INPUT TO VARIABLE ---------->*/
    let chibiCardName = document.getElementById("cardName").value;
    let chibiCard;

    /* ----------- CHECK IF INPUT IS VALID -----------> */
    for (let i = 1; i < chibisArray.length+2; i++) {
        if (i === 112) {
            $("#chibiCardImage").html(searchInstructions);
            $("#chibiCardStatus").html(`Pick a card !!`);
            $("#cardName").val("").attr("placeholer", "search by card name").focus();
            return;
        } else if (chibiCardName == chibisArray[i-1].name) {
            chibiCard = chibisArray[i-1].id;
            break;
        } else {
            continue;   
        }
    }

    $("#chibiCardStatus").html(`<img src="../static/css/loader.gif" alt="loading..." /> Searching !!`);
    
    /* ----------- LOAD CHIBI API -----------> */
    $.when (        
    $.getJSON(`https://chibifighters.com/api/stats/`)
    ).then(
        function(chibiApiResponse ) {
            let cardTypes = chibiApiResponse.types;
            $("#chibiCardImage").html(cardInfosHTML(chibiCard, cardTypes));           
        },        
        function(errorResponse) {
            if(errorResponse.status === 404) {
                $("#chibiData").html(
                    `<h2>Chibi Fighters down</h2>`);
            } else {
                $("#chibiData").html(
                    `<h2>Error: ${errorResponse.responseJSON.message}</h2>`);            
            }       
        });    
}

/*-------------------- CREATE CARDS BY STATS -------------------- */
function findCardsByStats(event){    

    /* ----------- DECLARE AND ASSIGN INPUT TO VARIABLES ---------->*/
    let chibiCardType = $("#cardType :selected").text();
    let chibiCardRarity = $("#cardRarity :selected").text();
    let chibiCardSource = $("#cardSource :selected").text();
    let chibiCardSet = $("#cardSet :selected").text();
    let chibiCard;
    let matchesArray = [];
    let matchesArrayTemp = [];
    let temp;
    $("#chibiCardStatus").html(`<img src="../static/css/loader.gif" alt="loading..." /> Searching !!`);
    $( "#chibiCardImage" ).empty(); 

    /* ----------- LOAD CHIBI API -----------> */
    $.when (        
    $.getJSON(`https://chibifighters.com/api/stats/`)
    ).then(
        function(chibiApiResponse ) {
            let cardTypes = chibiApiResponse.types;            

            /* ----------- FILL MATCHES ARRAY -----------> */
            for (let i = 1; i < chibisArray.length+1; i++) {
                matchesArray.push(i);
            }

            /* ----------- CHECK MATCHES ARRAY AGAINST TYPE -----------> */
            for (let i = 0; i < matchesArray.length; i++) {
                temp = matchesArray[i];
                if (chibiCardType == "all") {
                    matchesArrayTemp = matchesArray; // works in test, odd
                    break;                
                } else if (chibiCardType === chibisArray[temp-1].type) {
                    matchesArrayTemp.push(temp);
                }                
            }
            // matchesArrayTemp =[]; --> test variable
            if (matchesArrayTemp.length === 0) {
                $("#chibiCardImage").html(searchInstructions);
                $("#chibiCardStatus").html(`No such card !!`);
            } else {
                matchesArray = matchesArrayTemp;  // tested              
            }            
            
            /* ----------- CHECK MATCHES ARRAY AGAINST RARITY -----------> */            
            matchesArrayTemp = [];
            for (let i = 0; i < matchesArray.length; i++) {
                temp = matchesArray[i];
                if (chibiCardRarity == "all") {
                    matchesArrayTemp = matchesArray;
                    break;                
                } else if (chibiCardRarity == chibisArray[temp-1].rarity) {
                    matchesArrayTemp.push(temp);
                }                
            } // loop tested
            
            if (matchesArrayTemp.length == 0) {
                matchesArray = [];
                $("chibiCardImage").html("");
                $("#chibiCardImage").html(searchInstructions);
                $("#chibiCardStatus").html(`No such card !!`);
            } else {
                matchesArray = matchesArrayTemp;
            }            

            /* ----------- CHECK MATCHES ARRAY AGAINST SOURCE -----------> */
            matchesArrayTemp = [];
            for (let i = 0; i < matchesArray.length; i++) {
                temp = matchesArray[i];
                if (chibiCardSource === "all") {
                    matchesArrayTemp = matchesArray;
                    break;                
                } else if (chibiCardSource === chibisArray[temp-1].source) {
                    matchesArrayTemp.push(temp);
                }                
            }

            if (matchesArrayTemp.length === 0) {
                matchesArray = [];
                $("chibiCardImage").html("");
                $("#chibiCardImage").html(searchInstructions);
                $("#chibiCardStatus").html(`No such card !!`);
            } else {
                matchesArray = matchesArrayTemp;
            }

            /* ----------- CHECK MATCHES ARRAY AGAINST SET -----------> */
            matchesArrayTemp = [];
            for (let i = 0; i < matchesArray.length; i++) {
                temp = matchesArray[i];
                if (chibiCardSet === "all") {
                    matchesArrayTemp = matchesArray;
                    break;                
                } else if (chibiCardSet === chibisArray[temp-1].set) {
                    matchesArrayTemp.push(temp);
                }                
            }

            if (matchesArrayTemp.length == 0) {
                matchesArray = [];
                $("chibiCardImage").html("");
                $("#chibiCardImage").html(searchInstructions);
                $("#chibiCardStatus").html(`No such card !!`);
            } else {
                matchesArray = matchesArrayTemp;
            }
            
            /* ----------- RETURN MATCHES TO HTML -----------> */
            for (let i = 0; i < matchesArray.length; i++) {
                chibiCard = matchesArray[i];
                document.getElementById('chibiCardImage').innerHTML += cardInfosHTML(chibiCard, cardTypes);                
            }
        },        
        function(errorResponse) {
            if(errorResponse.status === 404) {
                $("#chibiData").html(
                    `<h2>Chibi Fighters down</h2>`);
            } else {
                $("#chibiData").html(
                    `<h2>Error: ${errorResponse.responseJSON.message}</h2>`);            
            }       
        });
}

/*-------------------- GENERATE SEARCH DROPDOWNS ON LOAD -------------------- */
function genDropdowns () {
    let tmpID, tmpVal, tmpType, tmpRarity, tmpSource, tempSet;    

    for (let i = 0; i < chibisArray.length; i++) {
        tmpVal = chibisArray[i].name;        
        document.getElementById('cards').innerHTML += `<option>${tmpVal}</option>`;
    }

    for (let i = 0; i < cardTypesArray.length; i++) {
        tmpType = cardTypesArray[i];        
        document.getElementById('cardType').innerHTML += `<option>${tmpType}</option>`;
    }
    
    for (let i = 0; i < cardRarityArray.length; i++) {
        tmpRarity = cardRarityArray[i];        
        document.getElementById('cardRarity').innerHTML += `<option>${tmpRarity}</option>`;
    }

    for (let i = 0; i < cardSourceArray.length; i++) {
        tmpSource = cardSourceArray[i];        
        document.getElementById('cardSource').innerHTML += `<option>${tmpSource}</option>`;
    }

    for (let i = 0; i < cardSetArray.length; i++) {
        tmpSet = cardSetArray[i];        
        document.getElementById('cardSet').innerHTML += `<option>${tmpSet}</option>`;
    }
}

/*-------------------- POPULATE SEARCH DROPDOWNS WHEN PAGE IS READY -------------------- */
$(document).ready(genDropdowns);