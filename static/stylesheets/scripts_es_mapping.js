$(document).ready(function () {

	$.validator.addMethod('sourceSeleceted',
        function(value) {
            return value == 'a' || value == 'b' || value == 'c';
        }, 'Select Source');

	$.validator.addMethod('speciesSelected',
        function(value) {
            return speciesSelectedFunc(value);
        }, 'Select One');

	function speciesSelectedFunc( value ) {
		var sourceId = $('#id_ES_source').val();
		console.log("sourceId = "+sourceId);
		if (sourceId == "a" && $('#id_a').val() !== "") {
			return true;
		}
		if (sourceId == "b" && $('#id_b').val() !== "") {
			return true;
		}
		if (sourceId == "c" && $('#id_c').val() !== "") {
			return true;
		}
		return false;
	}

	$.validator.addMethod('nsSelect',
        function(value) {
            return nsSelectFunc(value);
        }, 'Select One');

	function nsSelectFunc( value ) {
		var nsSelected = $('#id_a').val();
		if (nsSelected == "a1" && $('#id_a1').val() !== "") {
			return true;
		}
		if (nsSelected == "a3" && $('#id_a3').val() !== "") {
			return true;
		}
		if (nsSelected == "a4" && $('#id_a4').val() !== "") {
			return true;
		}
		if ($('#id_a').closest('tr').is(":hidden")) {
			return true;
		}
		else {
			return false;
		}
	}

	$.validator.addMethod('iucnSelect',
        function(value) {
            return iucnSelectFunc(value);
        }, 'Select One');

	function iucnSelectFunc( value ) {
		var iucnSelected = $('#id_b').val();
		if (iucnSelected == "b1" && $('#id_b1').val() !== "") {
			return true;
		}
		if (iucnSelected == "b2" && $('#id_b2').val() !== "") {
			return true;
		}
		if (iucnSelected == "b3" && $('#id_b3').val() !== "") {
			return true;
		}
		if (iucnSelected == "b4" && $('#id_b4').val() !== "") {
			return true;
		}
		if (iucnSelected == "b5" && $('#id_b5').val() !== "") {
			return true;
		}
		if (iucnSelected == "b6" && $('#id_b6').val() !== "") {
			return true;
		}
		if (iucnSelected == "b7" && $('#id_b7').val() !== "") {
			return true;
		}
		if (iucnSelected == "b8" && $('#id_b8').val() !== "") {
			return true;
		}
		if ($('#id_b').closest('tr').is(":hidden")) {
			return true;
		}
		else {
			return false;
		}
	}

	$.validator.addMethod('usfwsSelect',
        function(value) {
            return usfwsSelectFunc(value);
        }, 'Select One');

	function usfwsSelectFunc( value ) {
		var usfwsSelected = $('#id_c').val();
		if (usfwsSelected == "c1" && $('#id_c1').val() !== "") {
			return true;
		}
		if (usfwsSelected == "c2" && $('#id_c2').val() !== "") {
			return true;
		}
		if ($('#id_c').closest('tr').is(":hidden")) {
			return true;
		}
		else {
			return false;
		}
	}

	$.validator.messages.required = 'Required';

	var validator = $('form').validate({
        errorElement: "div",
        wrapper: "div",  // a wrapper around the error message
        ignore: 'input[type="button"],input[type="submit"]',
        rules: {
            ES_source: {
                required: true,
                sourceSeleceted: true
            },
            Crop: {
                required: true,
            },
            Pesticide: {
                required: true,
            },
            Year: {
                required: true,
                digits: true
            },
            NS: {
                speciesSelected: true,
            },
            NSM: {
                nsSelect: true,
            },
            NSF: {
                nsSelect: true,
            },
            NSP: {
                nsSelect: true,
            },
            IUCN: {
                speciesSelected: true,
            },
            IUCN_Amphibians: {
                iucnSelect: true,
            },
            IUCN_Birds: {
                iucnSelect: true,
            },
            IUCN_Mammals: {
                iucnSelect: true,
            },
            IUCN_Mammals_Marine: {
                iucnSelect: true,
            },
            IUCN_Coral: {
                iucnSelect: true,
            },
            IUCN_Reptiles: {
                iucnSelect: true,
            },
            IUCN_Seagrasses: {
                iucnSelect: true,
            },
            IUCN_SeaCucumbers: {
                iucnSelect: true,
            },
            IUCN_Mangrove: {
                iucnSelect: true,
            },
            IUCN_MarineFish: {
                iucnSelect: true,
            },
            USFWS_t: {
                speciesSelected: true,
            },
            USFWS_p: {
                usfwsSelect: true,
            },
            USFWS_l: {
                usfwsSelect: true,
            },
        }
    });

	$('#id_NS').attr('id', 'id_a').closest('tr').addClass('method_options').hide();
	$('#id_IUCN').attr('id', 'id_b').closest('tr').addClass('method_options').hide();
	$('#id_USFWS_t').attr('id', 'id_c').closest('tr').addClass('method_options').hide();

	$('#id_NSM').attr('id', 'id_a1').closest('tr').addClass('method_options').hide();
	//$('#id_NSB').attr('id', 'id_a2').closest('tr').addClass('method_options').hide();
	$('#id_NSF').attr('id', 'id_a3').closest('tr').addClass('method_options').hide();
	$('#id_NSP').attr('id', 'id_a4').closest('tr').addClass('method_options').hide();

	$('#id_IUCN_Amphibians').attr('id', 'id_b1').closest('tr').addClass('method_options').hide();
	$('#id_IUCN_Birds').attr('id', 'id_b2').closest('tr').addClass('method_options').hide();
	$('#id_IUCN_Mammals').attr('id', 'id_b3').closest('tr').addClass('method_options').hide();
	$('#id_IUCN_Mammals_Marine').attr('id', 'id_b4').closest('tr').addClass('method_options').hide();
	$('#id_IUCN_Coral').attr('id', 'id_b5').closest('tr').addClass('method_options').hide();
	$('#id_IUCN_Reptiles').attr('id', 'id_b6').closest('tr').addClass('method_options').hide();
	$('#id_IUCN_Seagrasses').attr('id', 'id_b7').closest('tr').addClass('method_options').hide();
	$('#id_IUCN_SeaCucumbers').attr('id', 'id_b8').closest('tr').addClass('method_options').hide();
	$('#id_IUCN_Mangrove').attr('id', 'id_b9').closest('tr').addClass('method_options').hide();
	$('#id_IUCN_MarineFish').attr('id', 'id_b10').closest('tr').addClass('method_options').hide();    

	$('#id_USFWS_p').attr('id', 'id_c1').closest('tr').addClass('method_options').hide();
	$('#id_USFWS_l').attr('id', 'id_c2').closest('tr').addClass('method_options').hide();


	$('#id_ES_source').change(function () {
		$('tr.method_options').hide();

		if ($(this).val() == "a") {
			$('#id_' + $(this).val()).closest('tr').show();
			$('#id_a').change(function () {

				if ($(this).val() == "a1") {

					$('#id_' + $(this).val()).closest('tr').show();
					//$('#id_a2').closest('tr').hide();
					$('#id_a3').closest('tr').hide();
					$('#id_a4').closest('tr').hide();
				}
				else if ($(this).val() == "a3") {
					$('#id_' + $(this).val()).closest('tr').show();
					$('#id_a1').closest('tr').hide();
					//$('#id_a2').closest('tr').hide();
					$('#id_a4').closest('tr').hide();
				} 
				else if ($(this).val() == "a4") {
					$('#id_' + $(this).val()).closest('tr').show();
					$('#id_a1').closest('tr').hide();
					//$('#id_a2').closest('tr').hide();
					$('#id_a3').closest('tr').hide();
				}

			});
		} 
		else if ($(this).val() == "b") {
			$('#id_' + $(this).val()).closest('tr').show();
			$('#id_b').change(function () {

				if ($(this).val() == "b1") {
					$('#id_' + $(this).val()).closest('tr').show();
					$('#id_b2').closest('tr').hide();
					$('#id_b3').closest('tr').hide();
					$('#id_b4').closest('tr').hide();
					$('#id_b5').closest('tr').hide();
					$('#id_b6').closest('tr').hide();
					$('#id_b7').closest('tr').hide();
					$('#id_b8').closest('tr').hide();
					$('#id_b9').closest('tr').hide();
					$('#id_b10').closest('tr').hide();                                                             
				}
				else if ($(this).val() == "b2"){
					$('#id_' + $(this).val()).closest('tr').show();
					$('#id_b1').closest('tr').hide();
					$('#id_b3').closest('tr').hide();
					$('#id_b4').closest('tr').hide(); 
					$('#id_b5').closest('tr').hide();
					$('#id_b6').closest('tr').hide();
					$('#id_b7').closest('tr').hide();
					$('#id_b8').closest('tr').hide();
					$('#id_b9').closest('tr').hide();
					$('#id_b10').closest('tr').hide();                                                             
				}
				else if ($(this).val() == "b3"){
					$('#id_' + $(this).val()).closest('tr').show();
					$('#id_b1').closest('tr').hide();
					$('#id_b2').closest('tr').hide();
					$('#id_b4').closest('tr').hide();
					$('#id_b5').closest('tr').hide();
					$('#id_b6').closest('tr').hide();
					$('#id_b7').closest('tr').hide();
					$('#id_b8').closest('tr').hide();
					$('#id_b9').closest('tr').hide();
					$('#id_b10').closest('tr').hide();                                        
				}
				else if ($(this).val() == "b4"){
					$('#id_' + $(this).val()).closest('tr').show();
					$('#id_b1').closest('tr').hide();
					$('#id_b2').closest('tr').hide();
					$('#id_b3').closest('tr').hide();
					$('#id_b5').closest('tr').hide();
					$('#id_b6').closest('tr').hide();
					$('#id_b7').closest('tr').hide();                                                 
					$('#id_b8').closest('tr').hide();
					$('#id_b9').closest('tr').hide();
					$('#id_b10').closest('tr').hide();                                       
				}
				else if ($(this).val() == "b5"){
					$('#id_' + $(this).val()).closest('tr').show();
					$('#id_b1').closest('tr').hide();
					$('#id_b2').closest('tr').hide();
					$('#id_b3').closest('tr').hide();
					$('#id_b4').closest('tr').hide();
					$('#id_b6').closest('tr').hide();
					$('#id_b7').closest('tr').hide();                                        
					$('#id_b8').closest('tr').hide();
					$('#id_b9').closest('tr').hide();
					$('#id_b10').closest('tr').hide();                                        
				}
				else if ($(this).val() == "b6"){
					$('#id_' + $(this).val()).closest('tr').show();
					$('#id_b1').closest('tr').hide();
					$('#id_b2').closest('tr').hide();
					$('#id_b3').closest('tr').hide();
					$('#id_b4').closest('tr').hide();
					$('#id_b5').closest('tr').hide();
					$('#id_b7').closest('tr').hide();
					$('#id_b8').closest('tr').hide();
					$('#id_b9').closest('tr').hide();
					$('#id_b10').closest('tr').hide();                                                                                
				}
				else if ($(this).val() == "b7"){
					$('#id_' + $(this).val()).closest('tr').show();
					$('#id_b1').closest('tr').hide();
					$('#id_b2').closest('tr').hide();
					$('#id_b3').closest('tr').hide();
					$('#id_b4').closest('tr').hide();
					$('#id_b5').closest('tr').hide();
					$('#id_b6').closest('tr').hide();
					$('#id_b8').closest('tr').hide();
					$('#id_b9').closest('tr').hide();
					$('#id_b10').closest('tr').hide();                                         
				}
				else if ($(this).val() == "b8"){
					$('#id_' + $(this).val()).closest('tr').show();
					$('#id_b1').closest('tr').hide();
					$('#id_b2').closest('tr').hide();
					$('#id_b3').closest('tr').hide();
					$('#id_b4').closest('tr').hide();
					$('#id_b5').closest('tr').hide();
					$('#id_b6').closest('tr').hide();   
					$('#id_b7').closest('tr').hide();
					$('#id_b9').closest('tr').hide();
					$('#id_b10').closest('tr').hide();                                          
				}
				else if ($(this).val() == "b9"){
					$('#id_' + $(this).val()).closest('tr').show();
					$('#id_b1').closest('tr').hide();
					$('#id_b2').closest('tr').hide();
					$('#id_b3').closest('tr').hide();
					$('#id_b4').closest('tr').hide();
					$('#id_b5').closest('tr').hide();
					$('#id_b6').closest('tr').hide();   
					$('#id_b7').closest('tr').hide();
					$('#id_b8').closest('tr').hide();
					$('#id_b10').closest('tr').hide();                    
				}
				else if ($(this).val() == "b10"){
					$('#id_' + $(this).val()).closest('tr').show();
					$('#id_b1').closest('tr').hide();
					$('#id_b2').closest('tr').hide();
					$('#id_b3').closest('tr').hide();
					$('#id_b4').closest('tr').hide();
					$('#id_b5').closest('tr').hide();
					$('#id_b6').closest('tr').hide();   
					$('#id_b7').closest('tr').hide();
					$('#id_b8').closest('tr').hide();
					$('#id_b9').closest('tr').hide();
				}
			});
		}
		else if ($(this).val() == "c") {
			$('#id_' + $(this).val()).closest('tr').show();
			$('#id_c').change(function () {

				if ($(this).val() == "c1") {

					$('#id_' + $(this).val()).closest('tr').show();
					$('#id_c2').closest('tr').hide();
				} 
				else if ($(this).val() == "c2") {
					$('#id_' + $(this).val()).closest('tr').show();
					$('#id_c1').closest('tr').hide();
				}
			});
		}
	});

	// $("input[value='Submit']").click(function (e) {
	// 	e.preventDefault();

	// 	var html_input = $("form").html();
	// 	localStorage.html_input=html_input;

	// 	  event.preventDefault();
	// 	  var html_new = $("form").serialize();

	// 	localStorage.html_new=html_new;
	// 	console.log(localStorage);
	// 	alert('HEY!');
	// });
	
});