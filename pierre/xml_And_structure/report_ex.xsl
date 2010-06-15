<?xml version="1.0" encoding="ISO-8859-1"?>

<xsl:stylesheet version="1.0"
		xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  
  <xsl:template match="/">
    <html>
      <body style='background-color:#222;'>
	<h1 style = 'color: #59652F; font-size: 35px; text-align: center;'>Raport SVG TEST</h1>
	<xsl:for-each select="tests"><!--OPEN TESTS -->
	  <xsl:for-each select="comparaison"><!-- OPEN COMPARAISON-->
	    <ol style='background-color:#59652F'><h3 style = 'color: #222; font-size: 21px; text-align: center;'>Liste des instances:</h3>
	    <xsl:for-each select="instances"><!-- OPEN INSTANCES-->
	      <xsl:for-each select="instance"><!-- OPEN INSTANCE-->
		<br />
		 <!--position:absolute;-->
		<div style=" width:40%; height:60%;top:120px ;left:50px; background-color:#59652F; border-style:solid; border-width:3px; width=30%"  >
		<li>instance</li>
		<ul>
		  <li> </li>
		  <xsl:for-each select="preprocessing"><!-- OPEN PREPROCESSING-->
		    <table border="1" bgcolor='#A1B55D'>
		      <tr>
			<th  bgcolor="#9acd32">Preprocessing</th>
		      </tr>
		      <xsl:for-each select="preprocess"><!-- OPEN PREPROCESS-->
		     	<tr>
			  <td > <xsl:value-of select="."/></td>
			</tr>
		      </xsl:for-each><!-- CLOSE PREPROCESS -->
		    </table>
		  </xsl:for-each><!-- CLOSE PREPROCESSING -->
		  <li> </li>
		  <table border="1" bgcolor='#A1B55D'>
		      <tr>
			<th  bgcolor="#9acd32">Capture</th>
		      </tr>
		  <xsl:for-each select="capture"><!-- OPEN CAPTURE-->
		   <tr>
			  <td > <xsl:value-of select="."/><br /></td>
		   </tr>
		  </xsl:for-each><!-- CLOSE CAPTURE -->
		  </table>
		  <xsl:for-each select="postprocessing"><!-- OPEN POSTPROCESSING-->
		    <li> </li>
		     <table border="1" bgcolor='#A1B55D'>
		      <tr>
			<th  bgcolor="#9acd32">Postprocessing</th>
		      </tr>
		    <xsl:for-each select="postprocess"><!-- OPEN POSTPROCESS-->
		      <tr>
			<td><xsl:value-of select="."/></td>
		      </tr>
		    </xsl:for-each><!-- CLOSE POSTPROCESS -->
		     </table>
		  </xsl:for-each><!--  CLOSE POSTPROCESSING-->
		</ul>
		</div>
	      </xsl:for-each>  <!-- CLOSE  INSTANCE-->
	      
	    </xsl:for-each> <!-- CLOSE INSTANCES-->
	    </ol>
	     <!--position:absolute;-->
	    <div style = " width:40%; height:20%;top:520px ;left:50px; background-color:#59652F; border-style:solid; border-width:3px; width=30%" >
	    <h3>result</h3>
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
	</xsl:for-each><!-- CLOSE TESTS -->
      </body>
    </html>
  </xsl:template>
  
</xsl:stylesheet>
