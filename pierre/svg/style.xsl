<?xml version="1.0" standalone="no"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">

  <!-- Add DOCTYPE -->
  <xsl:template match="/">
    <xsl:text disable-output-escaping="yes">
</xsl:text>
    <xsl:apply-templates/>
  </xsl:template>

<xsl:template match="*"> <xsl:copy><xsl:apply-templates/> </xsl:copy></xsl:template>