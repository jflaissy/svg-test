<?xml version="1.0" encoding="ISO-8859-1"?>

<xsl:stylesheet version="1.0"
		        xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  
  <xsl:template match="/">
    <html>
      <body>
	    <h1 style = ' font-size: 35px; text-align: center;'>Rapport SVG TEST</h1>
	    <xsl:for-each select="tests"><!--OPEN TESTS -->
	      <xsl:for-each select="test"><!--OPEN TEST -->
	        <xsl:for-each select="comparisons"><!-- OPEN COMPARAISONS-->
	          <xsl:for-each select="comparison"><!-- OPEN COMPARAISON-->
		        <h3 style = 'color: #222; font-size: 21px; text-align: center;'>Liste des instances:</h3>
		        <xsl:for-each select="instances"><!-- OPEN INSTANCES-->
		          <table><tr>
		              <xsl:for-each select="instance"><!-- OPEN INSTANCE-->
		                <td style='width=70%'>
			              <!--position:absolute;-->
			              <div style=" border-style:solid; border-width:3px; width=40%;"  > 
			                
			                <xsl:for-each select="instance_id"><h2 style = "color: #222; text-align: center;">Instance: <xsl:value-of select="."/></h2> </xsl:for-each>

			                <xsl:for-each select="preprocessing"><!-- OPEN PREPROCESSING-->
			                  <table border="1">
			                    <tr><th    colspan="2"><h3>Preprocessing</h3></th></tr>
			                    <xsl:for-each select="preprocess"><!-- OPEN PREPROCESS-->
			                      <tr>	<td><i>name</i></td>
                                        <td><i>parameters</i></td> </tr>
				                  <tr>
				                    <td><xsl:value-of select="name"/></td>
				                    <td><xsl:value-of select="parameters"/></td>
				                  </tr>
			                    </xsl:for-each><!-- CLOSE PREPROCESS -->
			                    <tr><td><i>output</i></td><td> <xsl:value-of select="output"/></td>
			                    </tr>
			                  </table>
			                </xsl:for-each><!-- CLOSE PREPROCESSING -->
			                <table border="1" width="100%">
			                  <tr>
			                    <th  colspan="2"><h3>Capture</h3></th>
			                  </tr>
			                  <tr>
			                    <td ><i>name</i></td>
			                    <td ><i>output</i></td>
			                  </tr>
			                  <xsl:for-each select="capture"><!-- OPEN CAPTURE-->
			                    <tr>
				                  <td > <xsl:value-of select="name"/></td>
				                  <td > <xsl:value-of select="output"/></td>
			                    </tr>
			                  </xsl:for-each><!-- CLOSE CAPTURE -->
			                </table>
			                <xsl:for-each select="postprocessing"><!-- OPEN POSTPROCESSING-->
			                  <table border="1" width="100%">
			                    <tr>
				                  <th colspan="2"><h3>Postprocessing</h3></th>
			                    </tr>
			                    <xsl:for-each select="postprocess"><!-- OPEN POSTPROCESS-->
				                  <tr>
                                    <!--				<th  colspan="2">Postprocess</th> -->
			                      </tr>
			      				  <tr>
				                    <td><i>name</i></td>
				                    <td><i>parameters</i></td>
			                      </tr>
				                  <tr>
				                    <td><xsl:value-of select="name"/></td>
				                    <td><xsl:for-each select="parameters"><xsl:value-of select="parameter"/> , </xsl:for-each></td>
				                  </tr>
			                    </xsl:for-each><!-- CLOSE POSTPROCESS -->
			                  </table>
			                </xsl:for-each><!--  CLOSE POSTPROCESSING-->
			              </div> 
		                </td>
		              </xsl:for-each>  <!-- CLOSE  INSTANCE-->
		          </tr></table>
		        </xsl:for-each> <!-- CLOSE INSTANCES-->
		        
		        <!--position:absolute;-->
                <center>
		          <div style = " width:40%; height:25%;top:520px ;left:50px; border-style:solid; border-width:3px; " >
		            <h3 style = 'font-size: 21px; text-align: center;'>Result</h3>
		            <table border="0">
		              <tr >
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
                </center>
	          </xsl:for-each><!-- CLOSE COMPARAISON -->
	        </xsl:for-each><!-- CLOSE COMPARAISONS -->
	      </xsl:for-each><!-- CLOSE TEST -->
	    </xsl:for-each><!-- CLOSE TESTS -->
	  </body>
    </html>
  </xsl:template>
  
</xsl:stylesheet>
