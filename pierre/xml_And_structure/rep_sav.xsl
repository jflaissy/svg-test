<?xml version="1.0" encoding="ISO-8859-1"?>

<xsl:stylesheet version="1.0"
xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

<xsl:template match="/">
  <html>
  <body>
  <h1>Raport SVG TEST</h1>

<h3>Preprocessing</h3>  
<table border="1">
    <tr bgcolor="#9acd32">
      <th>preprocess</th>
    </tr>
    <xsl:for-each select="tests/comparaison/instances/instance/preprocessing/preprocess">
    <tr>
      <td><xsl:value-of select="."/></td>
    </tr>
    
    </xsl:for-each>
  </table>
<h3>capture</h3>
<table border="1">
    <tr bgcolor="#9acd32">
      <th>capture</th>
    </tr>
    <xsl:for-each select="tests/comparaison/instances/instance/capture">
    <tr>
      <td><xsl:value-of select="."/></td>
    </tr>
    </xsl:for-each>
  </table>
<h3>postprocess</h3>
<table border="1">
    <tr bgcolor="#9acd32">
      <th>postprocess</th>
    </tr>
    <xsl:for-each select="tests/comparaison/instances/instance/postprocessing/postprocess">
    <tr>
      <td><xsl:value-of select="."/></td>
    </tr>
    </xsl:for-each>
  </table>

<h3>result</h3>
<table border="1">
    <tr bgcolor="#9acd32">
      <th>Valide?</th>
      <th>Message</th>
    </tr>
    <xsl:for-each select="tests/comparaison/result">
    <tr>
      <td><xsl:value-of select="valid"/></td>
      <td><xsl:value-of select="message"/></td>
    </tr>
    </xsl:for-each>
  </table>
  </body>
  </html>
</xsl:template>

</xsl:stylesheet>
