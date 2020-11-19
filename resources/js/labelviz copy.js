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
    entity_types: [
             {
      type   : 'date',
      labels : ['date'],
      bgColor: 'limegreen',
    },
        {
      type   : 'ANN0_Date',
      labels : ['ANN0_Date'],
      bgColor: 'limegreen',
    },
        {
      type   : 'ANN0_Cause',
      labels : ['ANN0_Cause'],
      bgColor: 'limegreen',
    },
        {
      type   : 'ANN0_Diagnostic_intervention',
      labels : ['ANN0_Diagnostic_intervention'],
      bgColor: 'limegreen',
    },
        {
      type   : 'ANN0_Description',
      labels : ['ANN0_Description'],
      bgColor: 'limegreen',
    },
            {
      type   : 'ANN0_Frequency',
      labels : ['ANN0_Frequency'],
      bgColor: 'limegreen',
    },
            {
      type   : 'ANN0_Location',
      labels : ['ANN0_Location'],
      bgColor: 'limegreen',
    },
            {
      type   : 'ANN0_Severity',
      labels : ['ANN0_Severity'],
      bgColor: 'limegreen',
    },
            {
      type   : 'ANN0_Trend',
      labels : ['ANN0_Trend'],
      bgColor: 'limegreen',
    },
            {
      type   : 'ANN0_Trigger',
      labels : ['ANN0_Trigger'],
      bgColor: 'limegreen',
    },
            {
      type   : 'ANN0_Effects',
      labels : ['ANN0_Effects'],
      bgColor: 'limegreen',
    },
            {
      type   : 'ANN0_Medication',
      labels : ['ANN0_Medication'],
      bgColor: 'limegreen',
    },
            {
      type   : 'ANN0_Other_treatment',
      labels : ['ANN0_Other_treatment'],
      bgColor: 'limegreen',
    },
            {
      type   : 'ANN0_Referral',
      labels : ['ANN0_Referral'],
      bgColor: 'limegreen',
    },
                {
      type   : 'ANN1_Pain',
      labels : ['ANN1_Pain'],
      bgColor: 'yellow',
    },
        {
      type   : 'ANN1_Date',
      labels : ['ANN1_Date'],
      bgColor: 'yellow',
    },
        {
      type   : 'ANN1_Cause',
      labels : ['ANN1_Cause'],
      bgColor: 'yellow',
    },
        {
      type   : 'ANN1_Diagnostic_intervention',
      labels : ['ANN1_Diagnostic_intervention'],
      bgColor: 'yellow',
    },
        {
      type   : 'ANN1_Description',
      labels : ['ANN1_Description'],
      bgColor: 'yellow',
    },
            {
      type   : 'ANN1_Frequency',
      labels : ['ANN1_Frequency'],
      bgColor: 'yellow',
    },
            {
      type   : 'ANN1_Location',
      labels : ['ANN1_Location'],
      bgColor: 'yellow',
    },
            {
      type   : 'ANN1_Severity',
      labels : ['ANN1_Severity'],
      bgColor: 'yellow',
    },
            {
      type   : 'ANN1_Trend',
      labels : ['ANN1_Trend'],
      bgColor: 'yellow',
    },
            {
      type   : 'ANN1_Trigger',
      labels : ['ANN1_Trigger'],
      bgColor: 'yellow',
    },
            {
      type   : 'ANN1_Effects',
      labels : ['ANN1_Effects'],
      bgColor: 'yellow',
    },
            {
      type   : 'ANN1_Medication',
      labels : ['ANN1_Medication'],
      bgColor: 'yellow',
    },
            {
      type   : 'ANN1_Other_treatment',
      labels : ['ANN1_Other_treatment'],
      bgColor: 'yellow',
    },
            {
      type   : 'ANN1_Referral',
      labels : ['ANN1_Referral'],
      bgColor: 'yellow',
    },

                     {
      type   : 'ANN2_Pain',
      labels : ['ANN2_Pain'],
      bgColor: 'lightblue',
    },
        {
      type   : 'ANN2_Date',
      labels : ['ANN2_Date'],
      bgColor: 'lightblue',
    },
        {
      type   : 'ANN2_Cause',
      labels : ['ANN2_Cause'],
      bgColor: 'lightblue',
    },
        {
      type   : 'ANN2_Diagnostic_intervention',
      labels : ['ANN2_Diagnostic_intervention'],
      bgColor: 'lightblue',
    },
        {
      type   : 'ANN2_Description',
      labels : ['ANN2_Description'],
      bgColor: 'lightblue',
    },
            {
      type   : 'ANN2_Frequency',
      labels : ['ANN2_Frequency'],
      bgColor: 'lightblue',
    },
            {
      type   : 'ANN2_Location',
      labels : ['ANN2_Location'],
      bgColor: 'lightblue',
    },
            {
      type   : 'ANN2_Severity',
      labels : ['ANN2_Severity'],
      bgColor: 'lightblue',
    },
            {
      type   : 'ANN2_Trend',
      labels : ['ANN2_Trend'],
      bgColor: 'lightblue',
    },
            {
      type   : 'ANN2_Trigger',
      labels : ['ANN2_Trigger'],
      bgColor: 'lightblue',
    },
            {
      type   : 'ANN2_Effects',
      labels : ['ANN2_Effects'],
      bgColor: 'lightblue',
    },
            {
      type   : 'ANN2_Medication',
      labels : ['ANN2_Medication'],
      bgColor: 'lightblue',
    },
            {
      type   : 'ANN2_Other_treatment',
      labels : ['ANN2_Other_treatment'],
      bgColor: 'lightblue',
    },
            {
      type   : 'ANN2_Referral',
      labels : ['ANN2_Referral'],
      bgColor: 'lightblue',
    },

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