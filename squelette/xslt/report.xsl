<?xml version="1.0" encoding="ISO-8859-1"?>

<xsl:stylesheet version="1.0"
		xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  
  <xsl:template match="/">
    <html>
      <body style='background-color:#222;'>
	<h1 style = 'color: #59652F; font-size: 35px; text-align: center;'>Raport SVG TEST</h1>
	<xsl:for-each select="tests"><!--OPEN TESTS -->
	  <xsl:for-each select="test"><!--OPEN TEST -->
	    <xsl:for-each select="comparisons"><!-- OPEN COMPARAISONS-->
	      <xsl:for-each select="comparison"><!-- OPEN COMPARAISON-->
		<ol style='background-color:#59652F'><h3 style = 'color: #222; font-size: 21px; text-align: center;'>Liste des instances:</h3>
		<xsl:for-each select="instances"><!-- OPEN INSTANCES-->
		  <table style="background-color:#59652F;"><tr>
		    <xsl:for-each select="instance"><!-- OPEN INSTANCE-->
		      <td style='width=70%'>
			<!--position:absolute;-->
			<div style=" background-color:#59652F; border-style:solid; border-width:3px; width=40%;"  > 
			  
			<li><xsl:for-each select="instance_id"><h2 style = "color: #222; text-align: center;">Instance: <xsl:value-of select="."/></h2> </xsl:for-each></li>
			<ul>
			  <li> </li>
			  <xsl:for-each select="preprocessing"><!-- OPEN PREPROCESSING-->
			    <table border="1" bgcolor='#A1B55D'>
			      <tr>
				<th  bgcolor="#ff1133"  colspan="2">Preprocessing</th>
			      </tr>
			      <tr>
			      <th   bgcolor="#9acd45" colspan="2">Preprocess</th>
			    </tr>
			      <tr>
				<th  bgcolor="#9acd32">name</th>
				<th  bgcolor="#9acd32">parameters</th>
			      </tr>
			      <xsl:for-each select="preprocess"><!-- OPEN PREPROCESS-->
				<tr>
				  <td><xsl:value-of select="name"/></td>
				  <td><xsl:value-of select="parameters"/></td>
				</tr>


			      </xsl:for-each><!-- CLOSE PREPROCESS -->
			      <tr>
			      <th  bgcolor="#9acd32" colspan="2">Output</th>
			    </tr>
			    <tr>
			      <th  colspan="2"><xsl:value-of select="output"/></th>
			    </tr>
			    </table>
			  </xsl:for-each><!-- CLOSE PREPROCESSING -->
			  <li> </li>
			  <table border="1" bgcolor='#A1B55D'>
			    <tr>
			      <th  bgcolor="#ff1133" colspan="2">Capture</th>
			    </tr>
			    <tr>
			    <th >Name</th>
			    <th >Output</th>
			    </tr>
			    <xsl:for-each select="capture"><!-- OPEN CAPTURE-->
			      <tr>
				<td > <xsl:value-of select="name"/></td>
				<td > <xsl:value-of select="output"/></td>
			      </tr>
			    </xsl:for-each><!-- CLOSE CAPTURE -->
			  </table>
			  <xsl:for-each select="postprocessing"><!-- OPEN POSTPROCESSING-->
			    <li> </li>
			    <table border="1" bgcolor='#A1B55D'>
			      <tr>
				<th  bgcolor="#ff1133"  colspan="2">Postprocessing</th>
			      </tr>
			      <xsl:for-each select="postprocess"><!-- OPEN POSTPROCESS-->
				<tr>
				<th  bgcolor="#9acd32"  colspan="2">Postprocess</th>
			      </tr>
			      				<tr>
				<th  bgcolor="#9acd32" >name</th>
				<th  bgcolor="#9acd32" >parameters</th>
				<th  bgcolor="#9acd32" >filters-id</th>
			      </tr>
				<tr>
				  <td><xsl:value-of select="name"/></td>
				   <td><xsl:for-each select="parameters"><xsl:value-of select="parameter"/> , </xsl:for-each></td>
				   <td><xsl:value-of select="filter_id"/></td>
				</tr>
			      </xsl:for-each><!-- CLOSE POSTPROCESS -->
			    </table>
			  </xsl:for-each><!--  CLOSE POSTPROCESSING-->
			</ul>
			</div> 
		      </td>
		    </xsl:for-each>  <!-- CLOSE  INSTANCE-->
		  </tr></table>
		</xsl:for-each> <!-- CLOSE INSTANCES-->
		</ol>
		<!--position:absolute;-->
		<div style = " width:40%; height:25%;top:520px ;left:50px; background-color:#59652F; border-style:solid; border-width:3px; " >
		  <h3 style = 'color: #222; font-size: 21px; text-align: center;'>result</h3>
		  <table border="1" bgcolor='#A1B55D'>
		    <tr bgcolor="#9acd32">
		      <th>Valide?</th>
		    <th>Message</th>
		    </tr>
		    <xsl:for-each select="result"><!-- OPEN RESULT-->
		      <tr>
			<td><xsl:value-of select="valid"/></td>
			<td><xsl:value-of select="message"/></td>
		      </tr>
		    </xsl:for-each><!--CLOSE RESULT -->
		  </table>
		</div>
	      </xsl:for-each><!-- CLOSE COMPARAISON -->
	    </xsl:for-each><!-- CLOSE COMPARAISONS -->
	      </xsl:for-each><!-- CLOSE TEST -->
	  </xsl:for-each><!-- CLOSE TESTS -->
	</body>
      </html>
  </xsl:template>
  
</xsl:stylesheet>
