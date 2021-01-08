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
    entity_types: [{ type: 'ANN1_personality', labels: ['ANN1_personality'], bgColor: 'limegreen',},{ type: 'ANN1_leadership', labels: ['ANN1_leadership'], bgColor: 'limegreen',},{ type: 'ANN1_recommendation', labels: ['ANN1_recommendation'], bgColor: 'limegreen',},{ type: 'ANN1_interp_relation', labels: ['ANN1_interp_relation'], bgColor: 'limegreen',},{ type: 'ANN1_growth', labels: ['ANN1_growth'], bgColor: 'limegreen',},{ type: 'ANN1_time_mgmt', labels: ['ANN1_time_mgmt'], bgColor: 'limegreen',},{ type: 'ANN1_clinical_skills', labels: ['ANN1_clinical_skills'], bgColor: 'limegreen',},{ type: 'ANN1_academic_exce', labels: ['ANN1_academic_exce'], bgColor: 'limegreen',},{ type: 'ANN1_motivation', labels: ['ANN1_motivation'], bgColor: 'limegreen',},{ type: 'ANN1_doubt_phrase', labels: ['ANN1_doubt_phrase'], bgColor: 'limegreen',},{ type: 'ANN1_community_invol', labels: ['ANN1_community_invol'], bgColor: 'limegreen',},{ type: 'ANN1_prof_invol', labels: ['ANN1_prof_invol'], bgColor: 'limegreen',},{ type: 'ANN1_irrelevant', labels: ['ANN1_irrelevant'], bgColor: 'limegreen',},{ type: 'ANN2_personality', labels: ['ANN2_personality'], bgColor: 'yellow',},{ type: 'ANN2_leadership', labels: ['ANN2_leadership'], bgColor: 'yellow',},{ type: 'ANN2_recommendation', labels: ['ANN2_recommendation'], bgColor: 'yellow',},{ type: 'ANN2_interp_relation', labels: ['ANN2_interp_relation'], bgColor: 'yellow',},{ type: 'ANN2_growth', labels: ['ANN2_growth'], bgColor: 'yellow',},{ type: 'ANN2_time_mgmt', labels: ['ANN2_time_mgmt'], bgColor: 'yellow',},{ type: 'ANN2_clinical_skills', labels: ['ANN2_clinical_skills'], bgColor: 'yellow',},{ type: 'ANN2_academic_exce', labels: ['ANN2_academic_exce'], bgColor: 'yellow',},{ type: 'ANN2_motivation', labels: ['ANN2_motivation'], bgColor: 'yellow',},{ type: 'ANN2_doubt_phrase', labels: ['ANN2_doubt_phrase'], bgColor: 'yellow',},{ type: 'ANN2_community_invol', labels: ['ANN2_community_invol'], bgColor: 'yellow',},{ type: 'ANN2_prof_invol', labels: ['ANN2_prof_invol'], bgColor: 'yellow',},{ type: 'ANN2_irrelevant', labels: ['ANN2_irrelevant'], bgColor: 'yellow',},
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