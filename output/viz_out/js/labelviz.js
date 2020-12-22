// Copyright (C) 2018 The MITRE Corporation. See the toplevel
// file LICENSE.txt for license terms.

// The brat stuff has all been imported. The variable docData
// contains the document material in Brat format.

var bratLocation = "brat_13";
head.js(
    // External libraries
    bratLocation + '/client/lib/jquery.min.js',
    bratLocation + '/client/lib/jquery.svg.min.js',
    bratLocation + '/client/lib/jquery.svgdom.min.js',

    // brat helper modules
    bratLocation + '/client/src/configuration.js',
    bratLocation + '/client/src/util.js',
    bratLocation + '/client/src/annotation_log.js',
    bratLocation + '/client/lib/webfont.js',

    // brat modules
    bratLocation + '/client/src/dispatcher.js',
    bratLocation + '/client/src/url_monitor.js',
    bratLocation + '/client/src/visualizer.js'
);

var webFontURLs = [
    bratLocation + '/static/fonts/Astloch-Bold.ttf',
    bratLocation + '/static/fonts/PT_Sans-Caption-Web-Regular.ttf',
    bratLocation + '/static/fonts/Liberation_Sans-Regular.ttf'
];


// I have to define the attribute types. For reasons I don't understand,
// the only way to have a non"warning" attribute value is to declare
// the value, and have its value be a non-empty Javascript object.
// AND it has to have the name attribute.

var collData = {
    entity_types: [{ type: 'ANN1_Fever', labels: ['ANN1_Fever'], bgColor: 'limegreen',},{ type: 'ANN1_Chill', labels: ['ANN1_Chill'], bgColor: 'limegreen',},{ type: 'ANN1_Cough', labels: ['ANN1_Cough'], bgColor: 'limegreen',},{ type: 'ANN1_Fatigue', labels: ['ANN1_Fatigue'], bgColor: 'limegreen',},{ type: 'ANN1_Nasal_obstruction', labels: ['ANN1_Nasal_obstruction'], bgColor: 'limegreen',},{ type: 'ANN1_Loss_of_appetite', labels: ['ANN1_Loss_of_appetite'], bgColor: 'limegreen',},{ type: 'ANN1_Diarrhea', labels: ['ANN1_Diarrhea'], bgColor: 'limegreen',},{ type: 'ANN1_Abdominal_pain', labels: ['ANN1_Abdominal_pain'], bgColor: 'limegreen',},{ type: 'ANN1_Nausea', labels: ['ANN1_Nausea'], bgColor: 'limegreen',},{ type: 'ANN1_Vomiting', labels: ['ANN1_Vomiting'], bgColor: 'limegreen',},{ type: 'ANN1_Sore_throat', labels: ['ANN1_Sore_throat'], bgColor: 'limegreen',},{ type: 'ANN1_Headache', labels: ['ANN1_Headache'], bgColor: 'limegreen',},{ type: 'ANN1_Myalgia', labels: ['ANN1_Myalgia'], bgColor: 'limegreen',},{ type: 'ANN1_Loss_of_taste', labels: ['ANN1_Loss_of_taste'], bgColor: 'limegreen',},{ type: 'ANN1_Loss_of_smell', labels: ['ANN1_Loss_of_smell'], bgColor: 'limegreen',},{ type: 'ANN1_Dyspnea', labels: ['ANN1_Dyspnea'], bgColor: 'limegreen',},{ type: 'ANN1_Chest_pain', labels: ['ANN1_Chest_pain'], bgColor: 'limegreen',},{ type: 'ANN1_Delirium', labels: ['ANN1_Delirium'], bgColor: 'limegreen',},{ type: 'ANN1_Hypersomnia', labels: ['ANN1_Hypersomnia'], bgColor: 'limegreen',},{ type: 'ANN1_Cyanosis', labels: ['ANN1_Cyanosis'], bgColor: 'limegreen',},{ type: 'ANN1_PHI', labels: ['ANN1_PHI'], bgColor: 'limegreen',},{ type: 'ANN2_Fever', labels: ['ANN2_Fever'], bgColor: 'yellow',},{ type: 'ANN2_Chill', labels: ['ANN2_Chill'], bgColor: 'yellow',},{ type: 'ANN2_Cough', labels: ['ANN2_Cough'], bgColor: 'yellow',},{ type: 'ANN2_Fatigue', labels: ['ANN2_Fatigue'], bgColor: 'yellow',},{ type: 'ANN2_Nasal_obstruction', labels: ['ANN2_Nasal_obstruction'], bgColor: 'yellow',},{ type: 'ANN2_Loss_of_appetite', labels: ['ANN2_Loss_of_appetite'], bgColor: 'yellow',},{ type: 'ANN2_Diarrhea', labels: ['ANN2_Diarrhea'], bgColor: 'yellow',},{ type: 'ANN2_Abdominal_pain', labels: ['ANN2_Abdominal_pain'], bgColor: 'yellow',},{ type: 'ANN2_Nausea', labels: ['ANN2_Nausea'], bgColor: 'yellow',},{ type: 'ANN2_Vomiting', labels: ['ANN2_Vomiting'], bgColor: 'yellow',},{ type: 'ANN2_Sore_throat', labels: ['ANN2_Sore_throat'], bgColor: 'yellow',},{ type: 'ANN2_Headache', labels: ['ANN2_Headache'], bgColor: 'yellow',},{ type: 'ANN2_Myalgia', labels: ['ANN2_Myalgia'], bgColor: 'yellow',},{ type: 'ANN2_Loss_of_taste', labels: ['ANN2_Loss_of_taste'], bgColor: 'yellow',},{ type: 'ANN2_Loss_of_smell', labels: ['ANN2_Loss_of_smell'], bgColor: 'yellow',},{ type: 'ANN2_Dyspnea', labels: ['ANN2_Dyspnea'], bgColor: 'yellow',},{ type: 'ANN2_Chest_pain', labels: ['ANN2_Chest_pain'], bgColor: 'yellow',},{ type: 'ANN2_Delirium', labels: ['ANN2_Delirium'], bgColor: 'yellow',},{ type: 'ANN2_Hypersomnia', labels: ['ANN2_Hypersomnia'], bgColor: 'yellow',},{ type: 'ANN2_Cyanosis', labels: ['ANN2_Cyanosis'], bgColor: 'yellow',},{ type: 'ANN2_PHI', labels: ['ANN2_PHI'], bgColor: 'yellow',},
    ],
  entity_attribute_types: [ {
    type: "Reason",
    name: "Reason", // Bug which requires both of these.
    values: {
      indication: {name: "indication"},
      contraindication: {name: "contraindication"},
      preexisting_condition_or_risk_factor: {name: "preexisting_condition_or_risk_factor"},
      manifestation_or_complication: {name: "manifestation_or_complication"},
      AE_rate_lteq_placebo: {name: "AE_rate_lteq_placebo"},
      AE_animal: {name: "AE_animal"},
      AE_from_drug_interaction: {name: "AE_from_drug_interaction"},
      general_term: {name: "general_term"},
      AE_from_off_label: {name: "AE_from_off_label"},
      AE_only_as_instruction: {name: "AE_only_as_instruction"},
      hypothetical_AE: {name: "hypothetical_AE"},
      AE_for_another_drug_in_class: {name: "AE_for_another_drug_in_class"},
      OD_or_withdrawal: {name: "OD_or_withdrawal"},
      from_drug_use: {name: "from_drug_use"},
      from_drug_component: {name: "from_drug_component"},
      class_effect: {name: "class_effect"},
      positive_dechallenge: {name: "positive_dechallenge"},
      other: {name: "other"}
    }
  } ]
};

head.ready(function() {
    // There's a timeout related to the Web font loading. 
    // The only way to disable it, because it's a private variable, is to
    // tell the visualizer that the fonts are already loaded. If your browser
    // respects @font-face in the CSS, then this is irrelevant.
    // one of the fonts that's used doesn't seem to load, but
    // which one it is seems to differ across browsers.
    Visualizer.areFontsLoaded = true;
    var dispatcher = Util.embed(
        // id of the div element where brat should embed the visualisations
        'vizdiv',
        // object containing collection data
        collData,
        // object containing document data
        docData,
        // Array containing locations of the visualisation fonts
        webFontURLs
    );
  // If I want to display a normalization, which I do, I have to
  // do with with hovers here. Someday.
  dispatcher.on('displaySpanComment',
                function(event, target, id, spanType, spanAttributeText, spanText, spanComment, spanCommentType, spanNormalizations) {
                  // Normalizations are [db, id, text]
                  // spanAttributeText is a list of text strings.
                  var t = [spanText + ":"];
                  for (var i = 0; i < spanAttributeText.length; i++) {
                    t.push(spanAttributeText[i] + ",");
                  }
                  if (spanNormalizations.length > 0) {
                    t.push("MeddDRA info:");
                    for (var i = 0; i < spanNormalizations.length; i++) {
                      if (i > 0) {
                        t.push("or");
                      }
                      t.push(spanNormalizations[i][2] + " (" + spanNormalizations[i][1] + ")");
                    }
                  }
                  $("#meddraCode").empty().show().text(t.join(" "));
                });
  dispatcher.on('hideComment', 
                function() {
                  $("#meddraCode").hide();
                });
});